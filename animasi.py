import streamlit as st
import time
import pandas as pd
from warna import highlight_xr

def display_animated_table(results_df):
    progress_placeholder = st.empty()  # Tempat untuk menampilkan animasi

    # Simulasi animasi untuk menampilkan hasil iterasi satu per satu
    for index in range(len(results_df)):
        # Tampilkan tabel hanya sampai baris saat ini
        progress_placeholder.dataframe(results_df.iloc[:index + 1])  
        time.sleep(0.5)  # Jeda untuk efek animasi

    # Setelah animasi selesai, ganti tabel dengan yang sudah di-highlight pada xr
    styled_table = results_df.style.apply(highlight_xr, axis=1)
    progress_placeholder.table(styled_table)  # Gantikan tabel pertama dengan tabel final yang di-highlight
