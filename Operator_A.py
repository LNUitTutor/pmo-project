# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:23:51 2019

@author: User
"""
import numpy as np

def operatorA_action(V0:np.poly1d, number:int)->list:
    """ Obtaining successive iterations Vm using the integral operator kernel """
    p = V0 # задаємо початкове наближення 
    t = np.array([1,0]) #t
    t1 = np.array([-1,1]) #1-t
    m = 1
    list_V = [] # список поліномів Vm
    list_V.append(V0)
    
    while m < number:
        first_int = np.polyint(np.polymul(t,p)) # інтегруємо першу частину
        first_addition = np.polymul(t1, first_int) # знаходимо перший доданок
        
        second_int = np.polyint(np.polymul(t1,p)) # знаходимо первісну
        second_addition = np.polymul(t, np.polysub(np.polyval(second_int,1), second_int)) # підставляємо межі інтегрування та знаходимо другий доданок
        
        Vm = np.polyadd(first_addition, second_addition) #сумуємо два доданки
        p = Vm # попередній поліном
        
        list_V.append(Vm)
        m += 1
        
    return list_V
