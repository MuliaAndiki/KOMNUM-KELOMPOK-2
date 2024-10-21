import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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