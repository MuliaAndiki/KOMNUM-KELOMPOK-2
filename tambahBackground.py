import base64

# Membaca gambar latar belakang dari file lokal
def load_background_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()  # Encode ke base64