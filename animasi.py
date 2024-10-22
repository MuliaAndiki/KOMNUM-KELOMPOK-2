import streamlit as st
import time
import pandas as pd

def display_animated_table(results_df):
    st.markdown("<h2 style='color: white;'>Hasil Iterasi:</h2>", unsafe_allow_html=True)  # Mengganti warna teks Hasil Iterasi menjadi putih
    progress_placeholder = st.empty()  # Tempat untuk menampilkan animasi

    # Simulasi animasi untuk menampilkan hasil iterasi satu per satu
    for index in range(len(results_df)):
        # Tampilkan tabel hanya sampai baris saat ini
        progress_placeholder.dataframe(results_df.iloc[:index + 1])  
        time.sleep(0.5)  # Jeda untuk efek animasi
