import numpy as np
#TODO:task2, обчислити скалярний добуток (Vi,Vj)

def FindScalarProduct(a,b): # функція, що шукає скалярний добуток
    product_arr = np.polymul(a,b) # перемножуємо 
    poduct_poly = np.poly1d(product_arr) # перетворюємо результат на поліном
    integral_poly = np.polyint(poduct_poly) # знаходимо інтеграл
    
    return integral_poly(1)-integral_poly(0) # від інтеграла в точці 1 - інтеграл в точці 0

