import numpy as np

# Fungsi input manual untuk definisi fungsi
def convert_function(user_input):
    # Mengganti ekspresi eksponensial
    user_input = user_input.replace('e', 'np.exp(1)')

    # Mengganti operator pangkat (^)
    user_input = user_input.replace('^', '**')
    
    # Mengganti fungsi trigonometri
    user_input = user_input.replace('sin', 'np.sin')
    user_input = user_input.replace('cos', 'np.cos')
    user_input = user_input.replace('tan', 'np.tan')

    # Mengganti ekspresi akar
    user_input = user_input.replace('sqrt', 'np.sqrt')

    # Mengganti ekspresi nilai x
    user_input = user_input.replace('x', '*x')

    # Menghapus tanda * jika x berada di depan e^, sin, cos, tan, dan -
    for func in ['np.e','xp(1)**', 'np.sin(', 'np.cos(', 'np.tan(', 'np.sqrt(','-', '- ']:
        user_input = user_input.replace(func + '*' , func)
        
    # Menghapus tanda * jika x berada di awal
    user_input = user_input.lstrip('*') 

    # Buat fungsi dari string
    def f(x):
        return eval(user_input)
    
    return f