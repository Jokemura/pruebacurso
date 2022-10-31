import csv
with open('data.csv', 'r') as file:
    reader= csv.reader(file)
    data=[]
    for i in reader:
        data.append(i)

data.pop(0)
suma=0
for j in data:
    suma += float(j[0]) if j[0] != '' else 0

print('Promedio de QuoteAmount es ', suma/len(data))

