import streamlit as st
from bisection import bisection_method
from convert import convert_function

# Fungsi untuk menampilkan hasil akar penyelesaian
def show_result(f, a, b, tol, max_iter):
    # Menjalankan metode bisection
    results = bisection_method(f, a, b, tol, max_iter)
    
    # Ambil akar dari hasil terakhir
    final_result = results[-1]  # Hasil terakhir dari iterasi
    root = final_result['xr']
    
    # Tampilkan hasil akar penyelesaian
    st.markdown(f"<h2 style='color: white;'>Akar Penyelesaian:</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Akar dari persamaan f(x) dalam interval [{a:}, {b:}] adalah: {root}</p>", unsafe_allow_html=True)
