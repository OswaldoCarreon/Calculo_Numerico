#Secante
import math
import xlsxwriter

lista = ["n","a","b","Relative Error"]
def write_excel(i,data,sheet):
    for j in range(len(data)):
        sheet.write(i,j,data[j])



def f(x):   return math.log(x-1)+ math.cos(x-1)


def Secante(f,a,b,tolerance):
    i = 1
    workbook = xlsxwriter.Workbook('Secante.xlsx')
    sheet = workbook.add_worksheet()
    for j in range(len(lista)):
        sheet.write(0,j,lista[j])
    
    relative_error = relative_error = abs((b-a)/abs(b))
    write_excel(i,[i,a,b,relative_error],sheet)
    
    while(relative_error > tolerance):
        temp = a
        a = b
        b = temp - ( f(temp)*(temp-b) ) / ( f(temp) - f(b))
        relative_error = relative_error = abs((b-a)/abs(b))
        i+=1
        write_excel(i,[i,a,b,relative_error],sheet)
    workbook.close()   
    return b
          
p0 = 1.3
p1 = 2
T = 1e-5
raiz = Secante(f,p0,p1,T)
print(raiz)