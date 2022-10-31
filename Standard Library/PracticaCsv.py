import csv

with open('Titanic.csv', 'r') as file:
    reader = csv.reader(file)
    datos = []
    for row in reader:
        datos.append(row)

datos.pop(0)

suma_edades = 0
total_mujeres = 0 
total_hombres = 0
total_sobrevivientes = 0
total_fallecidos = 0

for row in datos:
    suma_edades += float(row[5]) if row[5] != '' else 0
    if row[4] == 'male':
        total_hombres += 1
    else:
        total_mujeres += 1
    if row[1] == '0':
        total_fallecidos += 1
    else:
        total_sobrevivientes += 1

print(f"Promedio edad: {suma_edades/len(datos):.2f}")
print("Total hombres:", total_hombres)
print("Total mujeres:", total_mujeres)
print("Total sobrevivientes:", total_sobrevivientes)
print("Total fallecidos:", total_fallecidos)