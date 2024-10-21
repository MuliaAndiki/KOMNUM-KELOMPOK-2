import streamlit as st

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