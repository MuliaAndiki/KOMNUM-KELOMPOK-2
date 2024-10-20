import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import base64

# Fungsi untuk menambahkan gambar latar belakang dari file lokal
def add_bg_from_local(image_file):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{image_file});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .stTitle {{
            color: white;  /* Warna font putih */
            font-weight: bold;  /* Membuat font tebal */
        }}
        .stTextInput, .stNumberInput {{
            font-weight: bold;  /* Membuat input tebal */
            color: white;  /* Warna font input putih */
        }}
        .stTextInput label, .stNumberInput label {{
            color: white;  /* Warna label input putih */
            font-weight: bold;  /* Membuat label tebal */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Bayangan pada label */
        }}
        .stTable {{
            font-weight: bold;  /* Membuat teks tabel tebal */
            color: white;  /* Warna font tabel putih */
            border-color: white;  /* Warna garis tabel putih */
        }}
        .stMarkdown, .stTable th, .stTable td {{
            color: white;  /* Warna teks tabel dan markdown putih */
            font-weight: bold;  /* Membuat teks tabel tebal */
            border: 2px solid white;  /* Membuat garis tabel tebal dan putih */
        }}
        /* Tambahkan efek bayangan pada teks judul */
        h1, h2 {{
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Bayangan pada judul */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Membaca gambar latar belakang dari file lokal
def load_background_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()  # Encode ke base64

# Path file gambar latar belakang
bg_image_path = "iofi1.png"  # Pastikan file ini ada di folder yang sama

# Memuat gambar latar belakang
bg_image = load_background_image(bg_image_path)

# Menambahkan gambar latar belakang
add_bg_from_local(bg_image)

# Fungsi input manual untuk definisi fungsi
def input_function(user_input):
    # Mengganti ekspresi eksponensial
    user_input = user_input.replace('e', 'np.exp(1)')

    # Mengganti operator pangkat (^)
    user_input = user_input.replace('^', '**')
    
    # Mengganti fungsi trigonometri
    user_input = user_input.replace('sin', 'np.sin')
    user_input = user_input.replace('cos', 'np.cos')
    user_input = user_input.replace('tan', 'np.tan')

    # Mengganti ekspresi nilai x
    user_input = user_input.replace('x', '*x')

    # Menghapus tanda * jika x berada di depan e^, sin, cos, tan
    for func in ['np.e','xp(1)**', 'np.sin(', 'np.cos(', 'np.tan(', '-', '- ']:
        user_input = user_input.replace(func + '*' , func)
        
    # Menghapus tanda * jika x berada di awal
    user_input = user_input.lstrip('*') 

    # Buat fungsi dari string
    def f(x):
        return eval(user_input)
    
    return f

# Metode Bisection
def bisection_method(f, a, b, tol, max_iter):
    iterations = []
    for n in range(1, max_iter + 1):
        xr = (a + b) / 2
        f_a = f(a)
        f_b = f(b)
        f_xr = f(xr)

        iteration = {
            'Iterasi': n,
            'a': a,
            'b': b,
            'F(a)': f_a,
            'F(b)': f_b,
            'xr': xr,
            'F(xr)': f_xr,
            'F(xr)*F(a)': f_xr * f_a,
            '|b-a|': abs(b - a)
        }
        iterations.append(iteration)

        if abs(f_xr) < tol:
            break

        if f_xr * f_a < 0:
            b = xr
        else:
            a = xr

    return iterations

# Fungsi untuk menampilkan grafik
def plot_graph(f):
    x = np.linspace(-10, 10, 400)  
    plt.figure(figsize=(8, 6))
    plt.plot(x, f(x), label='f(x)', color='#D81B60')  # Warna grafik
    plt.axhline(y=0, color='red', linestyle='--', label='y=0')
    plt.xlabel('x', color='white')  # Warna label sumbu x
    plt.ylabel('f(x)', color='white')  # Warna label sumbu y
    plt.title('Graph of f(x)', color='white')  # Warna judul grafik
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Bagian aplikasi Streamlit
st.markdown("<h1 style='color: white; font-weight: bold;'>Metode Bisection - Kelompok 2</h1>", unsafe_allow_html=True)

# Input pengguna
user_input = st.text_input("Masukkan fungsi f(x):", "x**2 - 4*x + 3")
a = st.number_input("Masukkan nilai a (batas bawah):", value=-2.0)
b = st.number_input("Masukkan nilai b (batas atas):", value=5.0)
tol = st.number_input("Masukkan nilai toleransi (tol):", value=1e-5)
max_iter = st.number_input("Masukkan nilai maksimum iterasi:", value=100)

if st.button("Jalankan Metode Bisection"):
    f = input_function(user_input)  # Konversi input fungsi
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

    # Tampilkan grafik fungsi f(x)
    plot_graph(f)