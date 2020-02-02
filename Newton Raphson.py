#Newton raphson
import math
#import sympy as sy
from scipy.misc import derivative

def f(x):   return math.log(x-1)+ math.cos(x-1)
def g(x):   return (x-2)**2-math.log(x)
def h(x):   return 2*x*math.cos(2*x)-(x-2)**2

def Newton_Raphson(f,pn,tolerance):
    i = 0
    pn_1 = pn #Punto anterior
    pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
    relative_error = abs((pn-pn_1)/(abs(pn)))

    #escribir en excel
    while(relative_error > tolerance):
        pn_1 = pn
        pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
        relative_error = (pn-pn_1)/(abs(pn))
        i+=1
    return pn
        
x = 1
T = 1e-5
raiz = Newton_Raphson(g,x,T)
print(raiz)





