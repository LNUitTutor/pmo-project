import numpy as np

def scalar_product(a_poly:np.ndarray, b_poly:np.ndarray)->float: 
    """Find scalar product of two polynomials"""
    integral = np.polyint(np.polymul(a_poly, b_poly)) # множимо поліноми і знаходимо первісну
    return integral(1) - integral(0) # від інтегралу в точці 1 - інтеграл в точці 0
