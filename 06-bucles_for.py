# los bucles for van a recorrer el codigo o lo que queramos una serie de veces en base a un rango
# en el bucle la variable valores toma en cada iteracion cada valor de la palabra

palabra="Python"

for valores in palabra:
    print (valores)


#romper un bucle break

for valores in palabra:
    if valores=='t':
        break
    print(valores)

#trabjando el rango iterable con numeros

for valores in range(0,5): 
    print (valores)

for valores in range(8):
    print(valores)

#imprimr impares
for valores in range(1,8,2): #salta de dos en dos
    print (valores)

for valores in range(2,10,2):
    print (valores)

