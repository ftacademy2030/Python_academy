#cadenas de texto
texto1='mi primer texto'
print(texto1)
texto2='mi segundo texto con "comillas dobles"'
print(texto2)
texto3="mi terce texto al reves con 'comilla simples por dentro'"
print (texto3)

#cadenas multilineas
texto1="""lorem ipsu es un texto
de varias lineas
y con las comillas triples me permite hacerlo sin
problemas, parececido a los comentarios multilineas
"""
print(texto1)

#conversion



valor1="10"
print(int(valor1)*10)

#escapando

texto1='primera frase\nsegunda frase seguida pero con salto\ny tercera frase'
print(texto1)



#tabulando

texto1='el valor de la operacion =\t40'
print(texto1)

#print input
texto1="en un lugar de la mancha"
texto2="de cuyo nombre no quiero acordarme"
print(texto1,texto2,sep="|")

nombre=input('dime tu nombre:')
print(type(nombre))


#concatennar texto
print(texto1+','+texto2)
print(f'este es el primer verso del Quijote{texto1} y luego este es el segundo {texto2}')

#extraer un caracter
print(texto1[3])
print(texto1[-2])
print(texto1[:])
print(texto1[:5])
print(texto1[5:])
print(texto1[4:8:2])

#longitud de cadena

print(len(texto1))


