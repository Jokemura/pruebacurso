
f = open('Prueba.txt', 'w')
f.write('Hola esto eso es un texo escrito desde python')
f = open('Prueba.txt', 'r')
print(f.read())
f.close()