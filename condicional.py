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

#actividad numero 7
declaracion_renta = int (input('haga aqui su declaracion de renta'))
if declaracion_renta < 10000:
    pagar = 5 * declaracion_renta / 100
    print ('Tienes que pagar ', pagar)
elif declaracion_renta < 20000:
    pagar = (15 * declaracion_renta/ 100)
    print ('Tienes que pagar ', pagar)
elif declaracion_renta < 35000:
    pagar = (20 * declaracion_renta/ 100)
    print ('Tienes que pagar ', pagar)
elif declaracion_renta < 60000:
    pagar = (30 * declaracion_renta/ 100)
    print ('Tienes que pagar ', pagar)
else: pagar = (45 * declaracion_renta/ 100)
print ('Tienes que pagar ', pagar)

#actividad 8
calificacion = float(input('ingrese su calificacion correspondiente 0, 0.4 , 0.6'))
if calificacion==0:
    print ('tu nivel es inaceptable y te corresponde cobrar', calificacion * 2400 )
elif calificacion == 0.4:
    print ('tu nivel es aceptable y te corresponde cobrar', calificacion * 2400 )
elif calificacion == 0.6:
    print ('tu nivel es meritorio y te corresponde cobrar', calificacion * 2400 )
else: print('Ingrese un dato correcto')

#actividad 9 
edad = int (input('ingrese la edad '))
if edad <= 4:
    print('puede ingresar gratis')
elif edad >4 and edad <=18:
    print('tiene que pagar 5 E')   
else: print('tiene que pagar 10')

#actividad 10.
tipo_pizza = int (input('si quieres una pizza vegetariana escriba 1 si prefiere una tradicional escriba 0'))
if tipo_pizza == 1:
   ingrediente = int (input('la pizza vegana tiene dos opciones de ingredientes escribe 1 para Pimiento y 0 para tofu'))
   if ingrediente == 1:
        print('Su pizza es vegetariana con Pimiento, Mozzarella y Tomate')
   else: print('Su pizza es vegetariana con tofu, Mozzarella y Tomate')
else:
    ingrediente = int(input('Su pizza es tradicional tiene 3 opciones de ingredientes elija 1 para Peperoni,2 para jamon y 3 Salmon'))
    if ingrediente==1:
        print ('Su pizza tardicional con Peperoni, Mozarrella y tomate')
    elif ingrediente==2:
        print('Su pizza es tradicional con Jamon, Mozzarella y tomate')
    else: print('Su pizza es tradicional con Salmon')