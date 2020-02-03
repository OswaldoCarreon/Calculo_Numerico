#Newton raphson
import math
#import sympy as sy
from scipy.misc import derivative
import xlsxwriter

lista = ["n","Pn","Realtive Error"]
def write_excel(i,data,hoja):
    for j in range(len(data)):
        hoja.write(i,j,data[j])
        
        
#---------------------------------------------------------------------------
        
def f(x):   return math.log(x-1)+ math.cos(x-1)
def g(x):   return (x-2)**2-math.log(x)
def h(x):   return 2*x*math.cos(2*x)-(x-2)**2

def Newton_Raphson(f,pn,tolerance):
    workbook = xlsxwriter.Workbook("Newton Raphson.xlsx")
    sheet = workbook.add_worksheet()
    for j in range(len(lista)):
        sheet.write(0,j,lista[j])
        
    i = 1
    pn_1 = pn #Punto anterior
    pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
    relative_error = abs((pn-pn_1)/(abs(pn)))
    write_excel(i,[i,pn,relative_error],sheet)
    
    while(relative_error > tolerance):
        pn_1 = pn
        pn = pn_1 - (f(pn_1) / derivative(f,pn_1,dx=1e-6) ) #Punto nuevo
        relative_error = (pn-pn_1)/(abs(pn))
        i+=1
        write_excel(i,[i,pn,relative_error],sheet)
        
    workbook.close()
    return pn
        
x = 1.6
T = 1e-5
raiz = Newton_Raphson(f,x,T)
print(raiz)





