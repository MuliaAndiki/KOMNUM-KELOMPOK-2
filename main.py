import streamlit as st
import time
import pandas as pd
from style import add_bg_from_local
from tambahBackground import load_background_image
from convert import convert_function
from bisection import bisection_method
from result import show_result
from plot import plot_graph

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
a = st.number_input("Masukkan nilai a (batas bawah):", format="%.1f")
b = st.number_input("Masukkan nilai b (batas atas):", format="%.1f")
tol = st.number_input("Masukkan nilai toleransi (tol):", format="%.5f")
max_iter = st.number_input("Masukkan nilai maksimum iterasi:", value=0)

if st.button ("Tampilkan plot graph"):
    f = convert_function(user_input)  # Konversi input fungsi
    with st.spinner('Sedang memproses...'):
        time.sleep(1)  # Simulasi loading

    # Tampilkan grafik fungsi f(x)
    plot_graph(f)

if st.button("Jalankan Metode Bisection"):
    f = convert_function(user_input)  # Konversi input fungsi
    with st.spinner('Sedang memproses...'):
        time.sleep(1)  # Simulasi loading

    # Dapatkan hasil iterasi dari metode Bisection
    results = bisection_method(f, a, b, tol, max_iter)
    
    # Ubah hasil iterasi menjadi DataFrame agar mudah ditampilkan dalam tabel
    results_df = pd.DataFrame(results)
    
    # Tampilkan hasil iterasi di luar tabel
    st.markdown("<h2 style='color: white;'>Hasil Iterasi:</h2>", unsafe_allow_html=True)  # Mengganti warna teks Hasil Iterasi menjadi putih
    progress_placeholder = st.empty()  # Tempat untuk animasi
    for index, row in results_df.iterrows():
        progress_placeholder.table(results_df.iloc[:index + 1])  # Tampilkan tabel hingga baris saat ini
        time.sleep(0.5)  # Jeda untuk efek animasi

    show_result(f, a, b, tol, max_iter)

    # Tampilkan grafik fungsi f(x)
    plot_graph(f)
