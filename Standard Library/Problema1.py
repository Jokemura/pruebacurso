'''
scriba un programa en Python que acepte el perímetro de un círculo que escriba un usuario.

Finalmente el programa debe imprimir:

El valor de π con 7 decimales.
El valor del área de dicho círculo (con 3 decimales) así como el valor del radio de dicho círculo (con 2 decimales).
Pistas
'''

# import math
# perimetro = float(input('Ingrese el Perimetro: '))
# pi =round(math.pi, 7) 
# radio = round(perimetro / 2 *1, 2)
# print(pi)
# area =  round(pi * radio **2.3)
# print('PI 7 decimales', pi)
# print('Radio', radio)
# print('Area', area)

'''
El presente ejercicio se enfoca en la manipulación de fechas utilizando datetime (Documentación oficial)

Explore la documentación y escriba un programa Python para mostrar la fecha y la hora actuales bajo los siguientes formatos de ejemplo (imaginando hoy fuese 10 de septiembre del 2022):
10-09-22
10-09-2022
Hoy día es Saturday
10~09~2022
10-09-2022 14:20:51
En caso obtengan Hoy día es Sábado no habría problema alguno, no se evaluará lo referente a los idiomas.

Es importante mencionar que la exploración de la documentación es importante sobretodo cuando le toque explorar de un paquete que no sea popular

'''

from datetime import date, datetime
ahora = datetime.now()
ahora2 = date.today()

print(ahora2.strftime('%d-%m-%y'))
print(ahora.strftime('%d-%m-%Y'))
print("Hoy dia es", datetime.today().strftime('%A'))
print(ahora.strftime('%d~%m~%Y'))
print(ahora.strftime("%d-%m-%Y %H:%M:%S"))






