import streamlit as st
import cv2
import numpy as np

# Menampilkan kamera di Streamlit
def show_camera():
    st.title('Streamlit Camera Test')

    # Buka kamera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        st.error("Tidak dapat mengakses kamera.")
        return

    stframe = st.empty()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Tidak dapat membaca dari kamera.")
            break
        
        # Konversi frame ke format RGB untuk Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels='RGB', use_column_width=True)

        # Keluar dari loop jika tombol 'q' ditekan
        if st.button('Stop Camera'):
            break
    
    cap.release()

show_camera()
