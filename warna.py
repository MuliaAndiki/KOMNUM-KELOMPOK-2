import pandas as pd

def highlight_xr(df):
    """
    Fungsi untuk memberikan highlight kuning pada nilai 'xr' hanya di baris terakhir.
    """
    color = 'background-color: yellow'
    styles = pd.DataFrame('', index=df.index, columns=df.columns)  # Inisialisasi DataFrame untuk style

    # Hanya berikan highlight pada kolom 'xr' di baris terakhir
    styles.loc[df.index[-1], 'xr'] = color
    
    return styles
