# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:03:12 2019

@author: User
"""
import numpy as np

def zero_check(v:np.ndarray)->np.ndarray:
    """ Validation and correction or higher coefficient is not zero """
    i = 0
    while v[i] == 0:
        i += 1
    return v[i:]

def operatorA_action(V0:np.ndarray, number:int)->np.ndarray:
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
        res = zero_check(Vm) # перевірка чи старший коефіціент не дорівнєю 0
        p = res # попередній поліном
        
        list_V.append(res)
        m += 1
        
    return list_V

        
        