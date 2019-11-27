import numpy as np 

"""---Tusk 2---"""
def FindScalarProduct(a,b): # функція, що шукає скалярний добуток
    product_arr = np.polymul(a,b) # перемножуємо 
    poduct_poly = np.poly1d(product_arr) # перетворюємо результат на поліном
    integral_poly = np.polyint(poduct_poly) # знаходимо інтеграл
    
    return integral_poly(1)-integral_poly(0) # від інтеграла в точці 1 - інтеграл в точці 0

"""---Tusk 1---"""

#задаємо поліном
poly = []
print("Enter V_0: ")
stop = 1
while stop != 0:
    val = float(input("Enter coef of poly: "))
    poly.append(val)
    stop = int(input("If it was last coef of poly press 0: "))
#copy_poly = poly[::-1]
n = len(poly) - 1 
while poly[n] == 0:
    del poly[n]
    n-=1

#сворюємо V_1... V_n  зводимо до робочого вигляду  
list_poly = [] 
list_poly.append(poly)
size = int(len(poly)) 
#u = None
#res = 0
count = 0 
print(poly)
while count!=size:
    all_poly = np.array(list_poly)
    #poduct_poly = np.poly1d(list_poly) # перетворюємо результат на поліном
    local = np.polyint(all_poly[count])
    next_poly = np.delete(local,np.s_[size:]) # знаходимо інтеграл
    #flip_poly = np.flip(next_poly)
    #print(flip_poly)   
    print(next_poly)
    list_poly.append(next_poly)
    count+=1
    list_poly[count]

"""---Tusk 3---"""
#створюємо матриці 
all_poly = np.array(list_poly)
matrix_of_SCALAR = []
vector_res = []
vector_of_coef = []
for i in all_poly[1:]:
    row_of_matrix = []
    for j in all_poly[1:]:   
        row_of_matrix.append(FindScalarProduct(i,j))
    print("----------")
    print(row_of_matrix)
    vector_res.append(FindScalarProduct(all_poly[0],np.polymul(i,-1)))
    matrix_of_SCALAR.append(row_of_matrix)

#пошук коеф
vector_of_coef = np.linalg.solve(np.array(matrix_of_SCALAR),np.array(vector_res))
poly_for_roots = np.poly1d(vector_of_coef)
root = np.roots(poly_for_roots)


""""---Tusk 4---"""
#пошук z
rz = 0
count = 0
while size != 0:
    print("-----------------------------")
    print(all_poly[size])
    print(vector_of_coef[count])
    z_el = np.polymul(vector_of_coef[count],all_poly[size])
    print(z_el)
    rz = np.polyadd(z_el,rz) 
    size -=1
    count+=1
print(rz)

size_of_rz = len(rz)
count = 0

#пошук U 
res_u =""
while count!=size_of_rz:
    res_u = np.polymul(root,rz[count])
    count += 1

print(res_u)

#int_res_u = np.polymul(root,np.polyint(res_u))# інтеграл від U

