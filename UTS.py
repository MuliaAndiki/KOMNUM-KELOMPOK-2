import numpy as np
import matplotlib.pyplot as plt

# Input manual untuk definisi fungsi
def input_function():
    print("Masukkan fungsi f(x) :")
    user_input = input()
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

# Input parameter secara manual
f = input_function()  
a = float(input("Masukkan nilai a (batas bawah): "))
b = float(input("Masukkan nilai b (batas atas): "))
tol = float(input("Masukkan nilai toleransi (tol): "))
max_iter = int(input("Masukkan nilai maksimum iterasi: "))

# Menjalankan metode bisection
results = bisection_method(f, a, b, tol, max_iter)

# Menampilkan hasil iterasi
print(f"{'Iterasi':<8}{'  a':<10}{'  b':<10}{'F(a)':<10}{'F(b)':<10}{'xr':<10}{'F(xr)':<10}{'F(xr).F(a)':<12}{'|b-a|':<10}")
print("-" * 90)  
for row in results:
    print(f"{row['n']:<8}{row['a']:<10.2f}{row['b']:<10.2f}{row['F(a)']:<10.2f}{row['F(b)']:<10.2f}{row['xr']:<10.2f}{row['F(xr)']:<10.2f}{row['F(xr).F(a)']:<12.2f}{row['|b-a|']:<10.2f}")

# Plot grafik fungsi
x = np.linspace(0, 5, 100)
plt.plot(x, f(x))
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x)')
plt.grid(True)
plt.show()
