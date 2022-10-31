'''
Escriba un programa en Python para calcular el número de días entre dos fechas.
 No es necesario que use inputs para el ingreso de las fechas.'''

from datetime import datetime

birhtday = datetime()
hoy = datetime.today
difer = hoy - birhtday
print(f'Diferencia de dias',difer.days)
