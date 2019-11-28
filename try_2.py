import numpy as np


def scalar_product(a, b): # скалярний добуток
    a_poly = np.poly1d(a) # перетворення на поліном
    b_poly = np.poly1d(b) # перетворення на поліном
    integral = np.polyint(np.polymul(a_poly, b_poly)) # множимо і знаходимо невизначений інтеграл
    return integral(1) - integral(0) # від інтегралу в точці 1 - в точці 0 


def kernel(x, t): # умова ядра
    if t < x:
        return (1 - x) * t
    else:
        return (1 - t) * x


#def operator_a(arr):  # (інтегральний оператор)


def get_v(v0, amount):  # шукаємо поліноми
    result = np.array([v0]) # масив для поліномів, перший нам даний
    for i in range(amount):
        result = np.vstack((result, operator_a(result[i]))) # додаємо поліном в масив 
    return result


def get_matrix(v, amount): # створюємо матрицю для СЛАР
    result = np.zeros(amount * amount).reshape(amount, amount)# створюємо нульову матрицю 
    for i in range(amount): # заповнюємо симетричну матрицю скалярними добутками
        for j in range(amount):
            if i >= j:
                value = scalar_product(v[i], v[j]) 
                result[i, j] = value
                result[j, i] = value
    return result


def get_right_vector(v, amount): # вектор після = в СЛАР
    result = np.array([])
    for i in range(amount,0,-1)): # за формулою від найбільшого до найменшого
        result = np.append(result, -(scalar_product(v[0], v[i])))
    return result

def get_C(matrix, right_vector): # знаходимо коефіцієнти С
    c_arr = np.linalg.solve(matrix,right_vector)
    return c_arr

def get_mu(c_arr): # знаходимо всі корені
    mu_poly = np.poly1d(c_arr[::-1])#в формулі від найменшого до найбільшого
    mu_values = np.roots(mu_poly)
    return mu_values

def get_z(c, v, amount):# за формулою знаходимо всі z
    result = np.array([])

    for j in range(amount):
        val = 0
        for i in range(j):
            val += c[i] * v[j - i]
        result = np.append(result, val)

    return result


def get_u(z, mu, amount): # за ормулою знаходимо всі u
    result = np.array([])

    for n in range(amount - 1):
        val = 0
        for j in range(amount):
            val += pow(z[j], amount) * pow(mu[n], j + 1)
        result = np.append(result, val)

    return result
