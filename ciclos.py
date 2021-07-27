#actividad  1
palabra = input("Ingrese una palabra: ")
for i in range(10):
    print(palabra)

#actividad 2
edad = int(input("Ingrese su edad "))
for i in range(edad):
    print("usted ha cumlido" + str(i+1) + " años")

#Actividad 3
numeropositivo = int(input("ingrese un número entero positivo: "))
for i in range(1, numeropositivo+1, 2):
    print(i)

#Actividad 4
enteropositivo = int(input("ingrese un numero positivo: "))
for i in range(enteropositivo, -1, -1):
    print(i)

#actividad 5
inversion = float(input("cuanto va a invertir "))
interes = float(input("ingrese el interes anual "))
tiempo = int(input("Años de la inversion"))
for i in range(tiempo):
    inversion *= 1 + interes / 100 
    print("ganancia en Años" + str(i+1) , '   ' , str(round(inversion, 2)))
#actividad 9 
clave = "contraseña"
ingresoclave = ""
while ingresoclave != clave:
    ingresoclave = input('ingresa la clave')
print ('clave correcta')

#actividad 11
numero2 = int(input("ingrese un numero superior a 2 "))
mayor2 = 2
while numero2 % mayor2 != 0:
    mayor2 += 1
if  mayor2 == numero2:
    print(str(numero2) + " es primo")
else:
    print(str(numero2) + " no es primo")

palabradividir = input("ingrese una palabra ")
for rango in range(len(palabradividir)-1, -1, -1):
    print(palabradividir[rango])
#actividad 12
frase = input('escribe una oracion')
letra = input("escrib la letra que quieres buscar")
contando = 0
for rango in frase:
    if rango == letra:
        contando += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contando, frase))


#actividad 13
while True:
    palabra_con_ECO = input('escriba la palabra que quiera y para finalizar el progrema escriba salir')
    if palabra_con_ECO == "salir":
        break
    print(palabra_con_ECO)