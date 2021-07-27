#actividad 1
materias_del_curso = ["matematicas", "quimica" , "fisica" , "historia ", "lengua"]
print (materias_del_curso)

#actividad2
materia_curso = ["matematicas", "quimica" , "fisica" , "historia ", "lengua"]
for materia in materia_curso:
    print ('yo estudio', materia)

#actividad 3
materiacurso = ["matematicas", "quimica" , "fisica" , "historia ", "lengua"]
notas = []
for getmateria in materiacurso:
    nota = input("cual es tu nota " + getmateria)
    notas.append(nota)
for rango in range(len(materiacurso)):
    print('en ' + materiacurso[rango] + 'saco la siguiente nota' + notas[rango])

#actividad4
numerosganadores = []
for rango in range(4):
    numerosganadores.append(int(input('Cual es el numero ganador')))
numerosganadores.sort()
print('los numeros ganadores son'+ str(numerosganadores))

#actividad 5
numeros3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for rango in range(1, 10):
    print(numeros3[-rango])


    #actividad 7
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for rango in range(len(abecedario), 1, -1):
    if rango % 3 == 0:
        abecedario.pop(i-1)
print(abecedario)

#actividad 8

palabra = input('ingrese un apalabra')
ok_palabra = palabra
palabra = list(palabra)
ok_palabra = list(ok_palabra)
ok_palabra.reverse()
if palabra == ok_palabra:
    print("palabra es palíndromo")
else:
    print("palabra no es un palíndromo")

