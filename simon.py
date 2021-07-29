n = int(input('ingrese un numero'))
def sumas (n):
    s=0
    for i in range (n,0,-1):
        s= s+i
    return s
resultado1 = sumas(n)
print(resultado1)

def factorial (n):
    s=1
    for i in range (n,0,-1):
        s = s*i
    return s
resultado2 = factorial(n)
print(resultado2)
#si es par la suma de las funcion factorial y suma 
#si es impar producto de la factorial y suma 
def final (n):
    if n %2 ==0:
       resultado =  resultado1+resultado2
    else: resultado = resultado1*resultado2
    return resultado
resultado_final=final(n)
print(resultado_final)
   

