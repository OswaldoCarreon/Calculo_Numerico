#Newton raphson
import math
import sympy as sy
from scipy.misc import derivative



def f(x):   return math.log(x-1)+ math.cos(x-1)

def Newton_Raphson(f,pn,tolerance):
    i = 0
    pn_1 = pn #Punto anterior
    pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
    relative_error = (pn-pn_1)/(abs(pn))
    
    while(relative_error < tolerance):
        pn_1 = pn
        pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
        relative_error = (pn-pn_1)/(abs(pn))
        i+=1
        
    print(relative_error)
    print(pn)
    print(i)
    
    
x = 1.6
T = 1e-1
Newton_Raphson(f,x,T)





