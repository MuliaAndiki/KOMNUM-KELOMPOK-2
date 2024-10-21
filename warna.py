import pandas as pd

def highlight_xr(row):
    # Memeriksa apakah 'xr' adalah kolom di row
    styles = [''] * len(row)  # Inisialisasi style untuk setiap kolom

    # Memeriksa apakah 'xr' ada di indeks (kolom) row
    if 'xr' in row.index:  
        if row.name == 9:  # Baris ke-10 memiliki indeks 9 (indeks dimulai dari 0)
            styles[row.index.get_loc('xr')] = 'background-color: yellow'  # Sorot kolom xr di iterasi ke-10

    return styles
