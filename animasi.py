import streamlit as st
import pandas as pd
import time
from warna import highlight_xr

def display_animated_table(results_df):
    progress_placeholder = st.empty()  # Tempat untuk animasi

    # Simulasi animasi untuk menampilkan hasil iterasi satu per satu
    for index in range(len(results_df)):
        # Tampilkan tabel hingga baris saat ini
        progress_placeholder.dataframe(results_df.iloc[:index + 1])  # Tampilkan tabel hingga baris saat ini
        time.sleep(0.5)  # Jeda untuk efek animasi

    # Setelah animasi selesai, tambahkan highlight pada xr di iterasi terakhir
    styled_table = results_df.style.apply(highlight_xr, axis=1)
    st.dataframe(styled_table)  # Tampilkan styled table setelah animasi