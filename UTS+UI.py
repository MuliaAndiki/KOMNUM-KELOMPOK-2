import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import time

# Fungsi untuk animasi loading
def show_loading_animation(message):
    loading_window = tk.Toplevel()  
    loading_window.title("Loading")
    loading_window.geometry("500x150")  
    loading_window.configure(bg="white")
    
    loading_label = tk.Label(loading_window, text=message, font=("Arial", 20), bg="white")
    loading_label.pack(pady=20)

    # Animasi progress bar
    progress = ttk.Progressbar(loading_window, orient="horizontal", length=350, mode="determinate")
    progress.pack(pady=10)

    # Mengupdate progress bar
    for i in range(101):
        progress['value'] = i  
        loading_window.update()
        time.sleep(0.05)  # Penundaan untuk efek loading

    loading_window.destroy()  

# Fungsi input manual untuk definisi fungsi
def input_function():
    user_input = user_input_var.get()  
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
            'n': n,
            'a': a,
            'b': b,
            'F(a)': f_a,
            'F(b)': f_b,
            'xr': xr,
            'F(xr)': f_xr,
            'F(xr).F(a)': f_xr * f_a,
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

# Fungsi untuk menampilkan hasil ke tabel Treeview dengan animasi
def display_results_in_table_with_animation(results):
    for row in table.get_children():
        table.delete(row)

    for row in results:
        table.insert('', 'end', values=(
            row['n'], row['a'], row['b'], row['F(a)'], row['F(b)'], row['xr'], row['F(xr)'], row['F(xr).F(a)'], row['|b-a|']
        ))
        root.update_idletasks()  
        time.sleep(0.2)  

# Fungsi untuk menampilkan grafik
def plot_graph(f):
    x = np.linspace(-10, 10, 400)  
    plt.figure(figsize=(8, 6))
    plt.plot(x, f(x), label='f(x)', color='blue')
    plt.axhline(y=0, color='r', linestyle='--', label='y=0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Fungsi untuk menjalankan metode dan memperbarui hasil
def run_bisection():
    f = input_function()  
    a = float(a_entry.get())
    b = float(b_entry.get())
    tol = float(tol_entry.get())
    max_iter = int(iter_entry.get())
    
    # Tampilkan animasi loading saat proses dengan pesan "Membuat tabel"
    show_loading_animation("Create Table") 
    
    results = bisection_method(f, a, b, tol, max_iter)
    
    # Tampilkan hasil iterasi dalam tabel dengan animasi
    display_results_in_table_with_animation(results)
    
    # Tampilkan grafik f(x)
    plot_graph(f)

# Setup UI menggunakan Tkinter
root = tk.Tk()
root.title("Metode Bisection JEAY")

# Variabel untuk input fungsi
user_input_var = tk.StringVar()

# Frame untuk input dan kontrol
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Label dan Entry untuk input fungsi
tk.Label(input_frame, text="Masukkan fungsi f(x):").pack(pady=5)
tk.Entry(input_frame, textvariable=user_input_var).pack(pady=5)

# Label dan Entry untuk parameter a, b, tol, dan iterasi maksimum
tk.Label(input_frame, text="Masukkan nilai a (batas bawah):").pack(pady=5)
a_entry = tk.Entry(input_frame)
a_entry.pack(pady=5)

tk.Label(input_frame, text="Masukkan nilai b (batas atas):").pack(pady=5)
b_entry = tk.Entry(input_frame)
b_entry.pack(pady=5)

tk.Label(input_frame, text="Masukkan nilai toleransi (tol):").pack(pady=5)
tol_entry = tk.Entry(input_frame)
tol_entry.pack(pady=5)

tk.Label(input_frame, text="Masukkan nilai maksimum iterasi:").pack(pady=5)
iter_entry = tk.Entry(input_frame)
iter_entry.pack(pady=5)

# Tombol untuk menjalankan metode bisection
tk.Button(input_frame, text="Jalankan Metode Bisection", command=run_bisection).pack(pady=10)

# Treeview untuk menampilkan hasil iterasi dalam bentuk tabel
columns = ('Iterasi', 'a', 'b', 'F(a)', 'F(b)', 'xr', 'F(xr)', 'F(xr).F(a)', '|b-a|')
table = ttk.Treeview(input_frame, columns=columns, show='headings')

# Mengatur heading tabel
for col in columns:
    table.heading(col, text=col)

# Menentukan ukuran kolom tabel
for col in columns:
    table.column(col, width=100, anchor='center')

table.pack(pady=20)  # Pastikan ini dipanggil setelah pengaturan kolom

# Menyembunyikan jendela utama sebelum menampilkan animasi
root.withdraw()
show_loading_animation("Loading Kelompok 2")

# Menampilkan jendela utama setelah animasi
root.deiconify()

# Menjalankan UI
root.mainloop()
