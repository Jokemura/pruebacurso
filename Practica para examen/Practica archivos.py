import os 
os.system('cls')

f = open('Prueba.txt','w')
f.write('Hola este texto esta escrito desde python ')
f= open('Prueba.txt', 'r')
print(f.read())
f= open('Prueba.txt', 'a')
f.write('\n' +  'Esta es una segunda Linea')
f.close()
