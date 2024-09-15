import cv2

cap = cv2.VideoCapture(2)  # Ganti dengan indeks lain jika perlu

if not cap.isOpened():
    print("Tidak dapat mengakses kamera")
else:
    print("Kamera terdeteksi, menampilkan video")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Kamera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

