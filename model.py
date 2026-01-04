import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import librosa
import soundfile as sf
import pickle
import sys

SAMPLE_RATE = 16000

# -------- LOAD MODEL --------
model = tf.keras.models.load_model("BuzzSense_final_model.keras")

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

yamnet = hub.load("https://tfhub.dev/google/yamnet/1")

# -------- AUDIO --------
def load_wav(path):
    wav, sr = sf.read(path)
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    if sr != SAMPLE_RATE:
        wav = librosa.resample(wav, orig_sr=sr, target_sr=SAMPLE_RATE)
    return wav

def get_embedding(path):
    wav = tf.constant(load_wav(path), dtype=tf.float32)
    _, emb, _ = yamnet(wav)
    return tf.reduce_mean(emb, axis=0).numpy()

# -------- PREDICT --------
def predict(audio_path):
    emb = get_embedding(audio_path)
    probs = model.predict(emb[None, :])
    idx = np.argmax(probs)
    label = le.inverse_transform([idx])[0]
    confidence = probs[0][idx]
    return (label, confidence)