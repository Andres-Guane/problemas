#actividad  1 
nombre = input("ingresa tu nombre ")
numeronombre = int (input("ingrese un numero entero "))
repetirnombre = nombre * numeronombre
print ( repetirnombre)


 # actividad 2 en esta actividad me di cuenta que tenia que terner muy claro los metodos
 # y entonces decidi escribir los mas utilizados con el fin de mentalizarlos 
nombrecompleto = input ('ingrea tu nombre completo')
minusculas = (nombrecompleto.lower())
mayuscula = (nombrecompleto.upper())
primeramayuscula = (nombrecompleto.title())
print (minusculas)
print (mayuscula)
print (primeramayuscula)

#Actividad 3 volvi a usar metodos, cuando los conoces todo es mas facil
nombreletras = input ('ingrese su nombre')
nombremostrar = (nombreletras.upper())
numerodeletras = (len(nombreletras))
print (numerodeletras , nombremostrar)

#Actividad 4
telefono = input ('ingrese el numero de telefono con el codigo del pais')
telefonomostrar =  telefono [3:]
print (telefonomostrar)

#actividad 5 en esta activida me toco buscar en google como invertir una lista y encontre
#ottros metodos mediante el range 
#mediante el while 
#la funcion reversed
#3 y la slice que me parecio la mas facil donde solo poner los datos de inicio donde se detiene y el step
frase = input ('ingrese una frase')
fraseinvertida = frase [: : -1]
print (fraseinvertida)

#actividad 6
# no entendi como hacerlo
frase2 = input ('ingrese una frase con una letra en minuscula')

#actividad 7 aplique el metodo find dentor de una lista la cual la inicie en 0 y la termien en@
correo = input('ingrese su correo electronico')
correoguane = (correo [:correo.find('@')])
print (correoguane ,'@guane.com.co' )

# actividad 8 no pude encntrar como hacer para obtener los datos despues del valor que asigno
precio = input ('ingrese el precio del producto')
euros = precio [: precio.find('.')]
print (euros)