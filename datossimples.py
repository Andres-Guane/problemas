#Actividad numero 1
print ('Hola mundo')
#Actividad numero 2
mensaje = 'Hola mundo'
print (mensaje)
#Actividad numero 3
nombre = input ('ingrese nombre ')
print ('Hola ' + nombre)
#Actividad numero 4
print (((2+3)/(2*5))**2)
#Actividad numero 5
horas = float (input('ingrese el numero de horas trabajadas '))
valor = float (input('ingrese el valor de cada hora de trabajo '))
pagar = valor * horas
print ('total a pagar ', pagar)
#Actividad numero 6 facil por que en el mismo problema daban la formula
sumanumero = float (input('ingreso un numero entero que quiere sumar '))
resultado = sumanumero * (sumanumero + 1) / 2
print('este es el resultado', resultado)
#Actividad numero 7 ---presente problemas con la formula de la masa corporal
#la busque en internet y era masa = peso dividido por altura elevado al cuadrado 
peso = float(input('ingrese el peso '))
estatura = float (input('ingrese la estatura '))
masa =  (peso)/(estatura)**2
print (masa)
#Actividad numero 8 me presento error y me costo mucho por que olvidaba declaralos enteros
numero1 = int (input ('ingrese un numero entero '))
numero2 = int (input ('ingrese un segundo numero entero '))
cociente = numero1 // numero2
print (cociente)
#actividad 9 despues de buscar las formulas por internet logre ponerlas en codigo
inversion = float (input('ingrese el valos a invertir'))
interes = float (input('ingrese el interes anual'))
años = float (input('ingrese numero de años'))
interes = interes /100+1
ganancia = (inversion * (interes)** años)
print (ganancia) 
#actividad 10 en este codigo ya aplique el poner de tipo entero desde el principio
payasos = int(input("ingrese el numero de payasos "))
muñecas = int(input("ingresa número de muñecas "))

pesopayaso = 112
pesomuñeca = 75
payasototal = pesopayaso * payasos
muñecastotal = muñecas * pesomuñeca

pesoenvio = payasototal + muñecastotal

print("El peso total del paquete es " , (pesoenvio) , 'gramos')