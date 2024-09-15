import cv2

# Jumlah maksimum indeks kamera yang ingin diperiksa
max_camera_index = 10

def check_camera_indices(max_index):
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Kamera terdeteksi pada indeks {i}")
            cap.release()  # Lepaskan sumber daya setelah memeriksa
        else:
            print(f"Tidak ada kamera pada indeks {i}")

check_camera_indices(max_camera_index)

