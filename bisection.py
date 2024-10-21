# Metode Bisection
def bisection_method(f, a, b, tol, max_iter):
    iterations = []
    for n in range(1, max_iter + 1):
        xr = (a + b) / 2
        f_a = f(a)
        f_b = f(b)
        f_xr = f(xr)

        iteration = {
            'Iterasi': n,
            'a': a,
            'b': b,
            'F(a)': f_a,
            'F(b)': f_b,
            'xr': xr,
            'F(xr)': f_xr,
            'F(xr)*F(a)': f_xr * f_a,
            '|b-a|': abs(b - a)
        }
        iterations.append(iteration)

        if abs(b - a) < tol :
            break

        if f_xr * f_a < 0:
            b = xr
        else:
            a = xr

    return iterations