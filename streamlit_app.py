import cv2

# Coba berbagai indeks jika kamera default tidak berfungsi
camera_index = 0
cap = cv2.VideoCapture(camera_index)
while True:
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Tidak dapat mengakses kamera dengan indeks {camera_index}")
        camera_index =+ 1
    else:
        print(f"Kamera terdeteksi dengan indeks {camera_index}")
        break
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Kamera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
        cap.release()
   
