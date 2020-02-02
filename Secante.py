#Secante
import math

def f(x):   return math.log(x-1)+ math.cos(x-1)


def Secante(f,a,b,tolerance):
    relative_error = relative_error = abs((b-a)/abs(b))
    i = 0
    while(relative_error > tolerance):
        temp = a
        a = b
        b = temp - ( f(temp)*(temp-b) ) / ( f(temp) - f(b))
        relative_error = relative_error = abs((b-a)/abs(b))
        i+=1
        
    return b
          
p0 = 1.3
p1 = 2
T = 1e-5
raiz = Secante(f,p0,p1,T)
print(raiz)