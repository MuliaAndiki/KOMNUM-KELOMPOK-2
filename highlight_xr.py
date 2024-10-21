import streamlit as st

# Fungsi untuk menampilkan tabel dengan highlight pada baris terakhir
def show_table_with_highlight(df):
    last_index = df.index[-1]
    table_html = df.style.apply(
        lambda x: ['background-color: green' if x.name == last_index else '' for i in x], axis=1
    ).render()
    st.markdown(table_html, unsafe_allow_html=True)