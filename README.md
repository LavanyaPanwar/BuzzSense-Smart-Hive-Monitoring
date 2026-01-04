# BuzzSense:Smart Hive Monitoring 🐝

BuzzSense is a hive monitoring system designed to analyze **honeybee health and hive conditions** using **vibroacoustics** combined with **machine learning**. The system classifies hive conditions into **Good, Okay, or Bad**, helping in early detection of stress, disease, or environmental disturbances in beehives.

---

## 📌 Problem Statement

Traditional beehive monitoring relies heavily on manual inspection, which is time-consuming, intrusive, and often misses early warning signs of hive stress. BuzzSense aims to provide a **non-invasive, data-driven solution** by continuously monitoring hive vibrations and sounds to assess hive health automatically.

---

## 🎯 Objectives

- Develop a sound system using microphones for capturing the vibroacoustic of
  honeybees.
- Store and retrieve the sound captured from microphones.
- Data generation and analysis for the prediction of honeybees' health status.

---

## Key Features

- Non-invasive acoustic monitoring using hive audio
- Deep learning embeddings using **YAMNet**
- Classification of hive health into **Good / Okay / Bad**
- Simple **Tkinter-based GUI** for audio upload & prediction
- Scalable and low-cost deployment using edge devices (ESP32)

---

## Technical Approach

### Audio Processing

- Hive sounds captured using microphones
- Audio resampled and standardized before inference

### Feature Extraction

- Uses **YAMNet**, a pre-trained deep learning model for audio event classification which acts as a high-level feature extractor.
- Extracts **1024-dimensional embeddings**
- Captures complex acoustic patterns beyond MFCCs

### Machine Learning Pipeline

- Unsupervised clustering for unlabeled audio grouping
- Custom feed-forward neural network trained on embeddings
- Multi-class classification: **Good, Okay, Bad**

---

## 📈 Results

- **Training Accuracy:** 96.01%
- **Test Accuracy:** 92.4%
- Strong generalization on unseen hive audio samples

---

## 🛠️ Tech Stack

### Programming & ML

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow / Keras

### Audio & Signal Processing

- Librosa
- SciPy

### Hardware (Project Context)

- ESP32
- MAX9814 High Performance microphone
- DHT11 Temperature/Humidity Sensor
- SD Card
- Fan

### Tools & Platforms

- Google Colab
- Git & GitHub
- VS Code

---

## 🖥️ Project Structure

```text
BuzzSense_Lavanya/
├── assets/ # Images and UI assets for the app
│ ├── bg.png
│ ├── bg1.jpg
│ ├── bg2.jpg
│ ├── bg3.jpg
│ └── bg4.jpg
├── BuzzSense_final_model.keras # Trained Keras model for hive health
├── BuzzSense.weights.h5 # Model weights (if saved separately)
├── label_encoder.pkl # LabelEncoder for good/okay/bad mapping
├── model.py # Model loading and prediction utilities
├── ui.py # Streamlit / Tkinter / GUI code for BuzzSense
├── test_sample_1.wav # Example hive audio file
├── README.md # Project documentation
└── .gitignore # Git ignore rules
```

---

## 📊 Dataset

- Custom dataset created using real hive vibration/audio samples
  ⚠️ Due to size constraints, the full dataset is not included in this repository. Dataset can be shared upon request or via external storage.

---

## 🚀 How to Run the Project

- 1️⃣ Clone the Repository

  git clone https://github.com/LavanyaPanwar/BuzzSense-Smart-Hive-Monitoring.git
  cd BuzzSense-Smart-Hive-Monitoring

- 2️⃣ Install Dependencies

  pip install numpy pandas librosa scikit-learn tensorflow

- 3️⃣ Run the Application

  python ui.py

- 4️⃣ Test with Sample Audio

  Use test_sample_1.wav or your own hive audio recording.

  The system outputs the predicted hive condition

---

## 👩‍💻 Author

Lavanya Panwar

B.Tech Computer Science

Interest Areas: Machine Learning, Backend Development, AI for Social Impact

---

## 📬 Contact

For collaboration, feedback, or dataset access:

- GitHub: https://github.com/LavanyaPanwar

## 📜 License

This project is for academic and research purposes.
