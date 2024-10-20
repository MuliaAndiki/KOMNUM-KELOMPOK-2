import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Fungsi input manual untuk definisi fungsi
def input_function(user_input):
    return eval("lambda x: " + user_input)

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
    plt.plot(x, f(x), label='f(x)', color='blue')
    plt.axhline(y=0, color='red', linestyle='--', label='y=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

# Bagian aplikasi Streamlit
st.title("Metode Bisection - Kelompok 2")

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
    
    # Tampilkan tabel iterasi menggunakan st.table
    st.write("### Hasil Iterasi:")
    st.table(results_df)
    
    # Tampilkan grafik fungsi f(x)
    plot_graph(f)
