# notas =  [15,20,18]
# alumno = ["Marcelo", "José", "Juan"]
# alumnos_notas = sorted(list(zip(alumno, notas)))
# for cont, value in enumerate(alumnos_notas, start = 1):
#     print(cont, '->', value[0], ':', value[1])

# Escriba un generador que permita contar las letras de las palabras de una lista.

# Ejemplos:

# Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

# Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

from tracemalloc import start


a = "hunano"
def contapalabras(word):
    return {i : word.count(i)for i in word}
print(contapalabras(a))

def funcion_generador(colleccion):
    for i in colleccion:
        if i % 2 == 0:
            yield i + 2
        else:
            yield i + 1


def funcion_generador_contador(word):
    for i in word:
        yield i , word.count(i)

# Teniéndos los siguientes criterios:

# Desaprobado: nota < 11
# Destacado: nota > 16
# Aprobado: para el resto de casos


notas = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

def registrar_aprobados(alumnos_notas):
    for (alumno, nota) in alumnos_notas:
        if nota>11:
            yield alumno, nota, 'Desaprobado'
        elif nota >16:
            yield alumno, nota, 'Destacado'
        else:
            yield alumno, nota, "Aprovado"
for count, (nombre, nota, texto) in enumerate(registrar_aprobados(alumnos_notas), start= 1):
    print(count, '->', nombre, ':', nota, f"({texto})")


