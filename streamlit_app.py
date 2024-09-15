import cv2

# Menggunakan VideoCapture untuk mencoba berbagai indeks
for i in range(10):  # Uji beberapa indeks
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Kamera ditemukan pada indeks {i}")
        cap.release()
    else:
        print(f"Tidak ada kamera pada indeks {i}")
