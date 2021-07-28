n = int(input('ingrese un numero'))
def sumas (n):
    s=0
    for i in range (n,0,-1):
        s= s+i
    return s
resultado = sumas(n)
print(resultado)