import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from model import predict

# ---------------------------
# File upload & prediction
# ---------------------------
def upload_audio():
    file_path = filedialog.askopenfilename(
        title="Select Audio File",
        filetypes=[("Audio Files", "*.wav *.mp3 *.flac")]
    )

    if not file_path:
        return

    try:
        result = predict(file_path)
        raw_status = str(result[0]).lower().strip()

        if "good" in raw_status:
            status = "Good"
        elif "okay" in raw_status or "ok" in raw_status:
            status = "Okay"
        else:
            status = "Bad"

        result_label.config(
            text=f"Hive Health Status: {status}",
            fg=label_colors.get(status, "black")
        )
        # status = result[0]
        # result_label.config(
        #     text=f"Hive Health Status: {status}",
        #     fg=label_colors.get(status, "black")
        # )
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------------------
# Main Window
# ---------------------------
root = tk.Tk()
root.title("BuzzSense")
root.geometry("800x450")
root.resizable(False, False)
#root.configure(bg="white")

# ---------------------------
# Background Image
# ---------------------------
bg_image = Image.open("assets/bg4.jpg")
bg_image = bg_image.resize((800, 450))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)




# ---------------------------
# Heading
# ---------------------------
heading = tk.Label(
    root,
    text="BuzzSense: Smart Hive Monitoring",
    font=("Helvetica", 22, "bold"),
    bg="#291C0F",
    # bg="#0e2b2f",
    fg="white"
)
heading.pack(pady=(60, 20)) 

# ---------------------------
# Upload Button
# ---------------------------
# upload_btn = tk.Button(
#     root,
#     text="Upload Bee Audio File",
#     command=upload_audio,
#     font=("Helvetica", 16),
#     bg="#524029",
#     fg="white",
#     padx=12,
#     pady=4
# )
# upload_btn.pack(pady=(30,20))
upload_btn = tk.Button(
    root,
    text="Upload Bee Audio File",
    command=upload_audio,
    font=("Helvetica", 15),
    bg="#5C4529",
    fg="white",
    activebackground="#6B5132",
    activeforeground="white",
    padx=12,
    pady=4,
    relief="raised",
    bd=2
)
upload_btn.pack(pady=(30,20))



# ---------------------------
# Result Label
# ---------------------------
label_colors = {
    "Good": "green",
    "Okay": "orange",
    "Bad": "red"
}

result_label = tk.Label(
    root,
    text="Hive Health Status: ---",
    font=("Helvetica", 14),
    bg="#F3F0EB",
    fg="#2C2C2C",
    padx=12,
    pady=6
)
result_label.pack(pady=(30,20))

# ---------------------------
# Run App
# ---------------------------
root.mainloop()
