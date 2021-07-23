#actividad 1
edad = input('ingrese edad')
if int (edad) < 18:
    print ('usted es menor de edad')
else:   print('Usted es mayor de edad ')

# actividad 2
clave = input ('ingrese su clave')
clavealmacenada = 'andres12345'
if clave == clavealmacenada :
    print ('clave correcta')
else: print('clave erronea')

#actividad3
numero1 = float (input ('ingrese un numero'))
numero2 = float (input ('ingrese el segundo numero'))
if numero2 == 0:
    print ('no puedes dividir por 0')
else : print(numero1/numero2)

#actividad4
num = int(input('ingrese un numero'))
numpar = num % 2
if numpar == 0:
    print('el numero es par')
else: print('el numero es impar')

#actividad 5
edad2 = int(input('ingresa tu edad '))
ingresos = int(input('ingrese tus ingresos mensuales'))
if edad2 >16 and ingresos >= 1000:
    print('tienes que pagar')
else: print ('no tienes que pagar')

#actividad 6 en
nombre1 = input('ingrese nombre')
sexo = input ('digite el numero 1 si es hombre y el 2 si es mujer')
if sexo == 1:
     grupo = 'A'
     print ('tu grupo es el B')
else:  print  ('tu grupo es el A')   