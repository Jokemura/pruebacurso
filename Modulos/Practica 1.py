# #Ejercicio 1
# def funcion_decoradora(function_parametro):
#     def funcion_interna(numbers):
#         print('Inicio del calculo del promedio')
#         print(function_parametro(numbers))
#         print('el calulo ha finalizao')
#     return funcion_interna

# @funcion_decoradora
# def get_avg(numbers: list)-> float:
#     return sum(numbers)/len(numbers)

# list_numbers=[14, 20, 21, 11, 12]
# get_avg(list_numbers)

#Ejercicio 2

# def doble()->str:
#     a= float(input('Ingrese un numero para sacar el doble'))
#     return str(a*2)


# def duplicar_letras()->list:
#     palabra: str= input('Ingrese palabra: ')
#     res: list = []
#     for p in palabra:
#         res.append(p)
#         res.append(p)
#     return res

# def funcion_decoradora(Funcion_parametro):
#     def funcion_interna(a):
#         print('Estoy Decorando esta funcion')
#         Funcion_parametro(a)
#         print('termine de decorar')
#     return funcion_interna   

# @funcion_decoradora
# def show_number(n):
#         print(f'Ingresaste el numero: ', n)

# show_number(10)

# # show_number(45)
# a='1 2 3 4 5 6 '
# def funcion_ordenada(n):
#     test_list = list(n)
#     test_list2= []     
#     flag = 0
#     j = 1
#     while j < len(test_list2): 
#         for i in test_list:
#             if i == ' ':
#                 test_list.remove(i)
#             else:
#                 test_list2.append(i)
                            
#                 if(test_list2[j] < test_list2[j - 1]): 
#                     flag = 1
#                 j += 1
            
#     if (not flag) : 
#         print ("Si, lista Ordenada.") 
#     else : 
#         print ("No Lista Desornedada.")

# funcion_ordenada(a)

# def increasingString(string: str)->bool:
#     numbers:list[int] = [int(number) for number in string.split(' ')]

#     for i in range(1, len(numbers)):
#         if numbers [i-1] > numbers[i]:
#             return False
#     return True



# def funcion_Mayus(Funcion_Parametro):
#     def auxiliar(n):
#         o = Funcion_Parametro(n.upper)
#         return o
#     return auxiliar

# @funcion_Mayus
# def saludar(s: any)-> str:
#     return f'Hola, {s}'

# def bold(Fparam):
#     def aux(cadena):
#         print(f'<b>{Fparam(cadena)}</b>')
#     return aux

# def italic(Fparam):
#     def aux(cadena):
#         print(f'<i>{Fparam(cadena)}</i>')
#     return aux

# def underline(Fparam):
#     def aux(cadena):
#         print(f'<u>{Fparam(cadena)}</u>')
#     return aux    

# @underline
# @italic
# @bold
# def escribir(texto):
#     return texto

# escribir('AVC')

# lista = [15,20,18]
# names= ["Marcelo", "José", "Juan"]
# for i in zip(lista, names):
#     print (i)

# enumerados=['Hola', True, 5, 6.04]
# for coun, i in enumerate(enumerados, start = 10):
#     #Coun es el indice que enumerate
#     # i es el valor 
#     print(coun,'->', i)

