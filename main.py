import streamlit as st
import time
import pandas as pd
from style import add_bg_from_local
from tambahBackground import load_background_image
from convert import convert_function
from bisection import bisection_method
from plot import plot_graph
from warna import highlight_xr  # Import highlight_xr dari warna.py
from animasi import display_animated_table  # Pastikan ini diimpor jika animasi ada di file terpisah

# Path file gambar latar belakang
bg_image_path = "background.png"  # Pastikan file ini ada di folder yang sama

# Memuat gambar latar belakang
bg_image = load_background_image(bg_image_path)

# Menambahkan gambar latar belakang
add_bg_from_local(bg_image)

# Bagian aplikasi Streamlit
st.markdown("<h1 style='color: white; font-weight: bold;'>Metode Bisection - Kelompok 2</h1>", unsafe_allow_html=True)

# Input pengguna
user_input = st.text_input("Masukkan fungsi f(x):")
a = st.number_input("Masukkan nilai a (batas bawah):", format="%.2f")
b = st.number_input("Masukkan nilai b (batas atas):", format="%.2f")
tol = st.number_input("Masukkan nilai toleransi (tol):", format="%.5f")
max_iter = st.number_input("Masukkan nilai maksimum iterasi:", value=0)

if st.button("Tampilkan plot graph"):
    f = convert_function(user_input)  # Konversi input fungsi

    # Tampilkan grafik fungsi f(x)
    plot_graph(f)
    with st.spinner('Sedang memproses...'):
        time.sleep(1)  # Simulasi loading

if st.button("Jalankan Metode Bisection"):
    f = convert_function(user_input)  # Konversi input fungsi
    with st.spinner('Sedang memproses...'):
        time.sleep(3)  # Simulasi loading lebih lama untuk memastikan spinner muncul
    
    # Eksekusi metode bisection
    results = bisection_method(f, a, b, tol, max_iter)
    
    # Ubah hasil iterasi menjadi DataFrame
    results_df = pd.DataFrame(results)
    
    # Tampilkan hasil dengan animasi menggunakan fungsi display_animated_table
    display_animated_table(results_df)

    # Tampilkan plot grafik fungsi f(x)
    plot_graph(f)

    # Tambahkan penjelasan hasil iterasi di bawah tabel
    st.markdown("<h3 style='color: white;'>Penjelasan Hasil Iterasi:</h3>", unsafe_allow_html=True)

    # Mendapatkan nilai xr di iterasi terakhir
    xr_final = results_df['xr'].iloc[-1]  # Mengambil nilai xr dari baris terakhir
    iterasi_terakhir = len(results_df)  # Menghitung jumlah iterasi yang dilakukan
    
    # Menambahkan penjelasan detail
    st.write(f"Jumlah iterasi yang dilakukan: {iterasi_terakhir}")
    st.write(f"Nilai xr di iterasi terakhir: {xr_final}")
