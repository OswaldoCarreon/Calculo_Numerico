import math 
import xlsxwriter

def f(x): return 2 + math.cos((math.e**x)-2)-math.e**x
def g(x): return x-(2**-x)
def h(x): return math.e**x-x**2+(3*x)-2
def i(x): return 2*x*math.cos(2*x)-(x+1)**2
def j(x): return x*math.cos(x)-2*(x**2)+3*x-1
def k(x): return (x**3)-x-1
def r(x): return (x)**3 


lista = ["i","a","b","pm","f(a)","f(pm)","f(pm)*f(a)","|b-a|"]

def write_excel(i,data,sheet):
    for j in range(len(data)):
        sheet.write(i,j,data[j])
        
        
def biseccion_raices(a,b,precision,f,x):
    i=1
    while abs(a-b) >= precision:
        pm = (a+b)/2
        
        if(f(pm) > x):
            b = pm
        else:
            a = pm
        i+=1
        
    return pm
      

def biseccion(a,b,precision,f):
    i=1
    
    workbook = xlsxwriter.Workbook('Biseccion.xlsx')
    sheet = workbook.add_worksheet()
    for j in range(len(lista)):
        sheet.write(0,j,lista[j])
         
    while abs(a-b) > precision:
        pm = (a+b)/2
        fa = f(a)
        fpm = f(pm)
       
        write_excel(i,[i,a,b,pm,f(a),f(pm),f(pm)*f(a),abs(b-a)],sheet)

        if (fa*fpm) < 0:
            b = pm
        else:
            a = pm
        i+=1
    
    pm = (a+b)/2
    fa = f(a)
    fpm = f(pm)
    
    write_excel(i,[i,a,b,pm,f(a),f(pm),f(pm)*f(a),abs(b-a)],sheet)
    
    workbook.close()
    return pm

a = float(input())
b = float(input())
presicion = float(input())

raiz = biseccion(a,b,presicion,k)
#raiz = biseccion_raices(a,b,presicion,r,b)
#valor = ej(1.5)
#print(valor)
print("Raiz: ",raiz)