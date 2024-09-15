import streamlit as st
import os
import shutil
from PIL import Image
import cv2
import numpy as np
import torch
from ultralytics import YOLO  # Placeholder for YOLOv10, replace this when YOLOv10 is available

# Fungsi untuk menyimpan gambar yang di-upload dan labelnya
def save_uploadedfile(uploadedfile, label):
    if not os.path.exists('data/images'):
        os.makedirs('data/images')
    
    if not os.path.exists('data/labels'):
        os.makedirs('data/labels')

    # Simpan gambar
    image_path = os.path.join('data/images', uploadedfile.name)
    with open(image_path, "wb") as f:
        f.write(uploadedfile.getbuffer())

    # Simpan label dalam format YOLO
    label_path = os.path.join('data/labels', uploadedfile.name.replace('.jpg', '.txt'))
    
    # Simulasi bounding box, class ID (0: OK, 1: Reject)
    if label == 'OK':
        class_id = 0
    elif label == 'Reject':
        class_id = 1
    
    # Bounding box simulasi (x_center, y_center, width, height)
    bbox = '0.5 0.5 0.5 0.5'
    with open(label_path, 'w') as f:
        f.write(f'{class_id} {bbox}\n')

    return st.success(f"Gambar '{uploadedfile.name}' berhasil disimpan dengan label '{label}'.")

# Fungsi untuk melatih model YOLOv5 atau YOLOv10 (saat tersedia)
def train_yolo():
    st.write("Pelatihan YOLOv10 dimulai...")

    # Copy data ke dalam folder yang sesuai dengan format YOLO
    if not os.path.exists('yolo_data'):
        os.makedirs('yolo_data')
    shutil.copytree('data/images', 'yolo_data/images/train', dirs_exist_ok=True)
    shutil.copytree('data/labels', 'yolo_data/labels/train', dirs_exist_ok=True)

    # Menjalankan pelatihan YOLOv5 (ganti dengan YOLOv10 ketika tersedia)
    os.system('python yolov5/train.py --img 640 --batch 16 --epochs 10 --data custom_dataset.yaml --weights yolov5s.pt')

    st.success("Model YOLO selesai dilatih!")

# Sidebar dengan menu
st.sidebar.title("Menu")
menu = st.sidebar.selectbox("Pilih Menu", ["Train", "Start"])

# Menu untuk training
if menu == "Train":
    st.title("Pelatihan Model Deteksi Barang dengan YOLO")
   
    # Upload gambar barang OK
    uploaded_ok = st.file_uploader("Upload gambar barang OK", type=['png', 'jpg', 'jpeg'], key="ok")
    if uploaded_ok is not None:
        save_uploadedfile(uploaded_ok, 'OK')

    # Upload gambar barang Reject
    uploaded_reject = st.file_uploader("Upload gambar barang Reject", type=['png', 'jpg', 'jpeg'], key="reject")
    if uploaded_reject is not None:
        save_uploadedfile(uploaded_reject, 'Reject')

    # Tombol untuk melatih model
    if st.button('Latih Model'):
        train_yolo()

# Menu untuk memulai deteksi objek secara real-time
elif menu == "Start":
    st.title("Deteksi Objek Real-Time dengan Model YOLO")

    # Pilih model yang sudah dilatih
    model_path = st.text_input("Masukkan path model YOLO yang telah dilatih", "yolov5s.pt")

    # Tombol untuk memulai deteksi real-time
    if st.button("Mulai Deteksi"):
        st.write("Memulai deteksi...")

        # Load model YOLO (YOLOv10 saat tersedia, menggunakan YOLOv5/8 sebagai placeholder)
        model = YOLO(model_path)

        # Akses webcam
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Deteksi objek dengan YOLO
            results = model(frame)

            # Visualisasi hasil deteksi
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    conf = box.conf[0]
                    label = result.names[int(box.cls[0])]
                    
                    # Gambar kotak bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Tampilkan frame di Streamlit
            stframe.image(frame, channels="BGR")

        cap.release()
        #cv2.destroyAllWindows()
