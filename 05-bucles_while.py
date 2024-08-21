#bucles es repetir una rutina o codigo durante el tiempo

#sentencia while se repite mientras se cumple una condicion.

condicion='S'

while condicion=='S':
    print('hola buenas tardes')
    condicion=input('quieres otro saludo? S/N: ')

print('Hasta otra amigo')


#break para romper una condicion

condicion='S'
valor=0
while condicion=='S':
    print('hola que tal')
    valor +=1
    if valor==5:
        print(f'te he saludado {valor} veces')
        break
print('que tengas un buen dia')    

#si usamos continue en lugar de salir estaremos indicando al sistema que continue

while True:
    nota=float(input('Introducza una nota: '))
    if nota<=0 or nota >=5:
        print('nota esta fuera de rango')
        break
    print(nota)


while True:
    print('MENU DE LA APLICACION')
    print(
    '''
    1-Entrar
    2-Salir
    ''')
    opcion=int(input('Seleccione una opcion: '))
    if opcion==1:
        print('1-Entrar')
        print(
        '''
        1-Saludar
        2-Salir
        '''
        )
        opcion1=int(input('seleccione opcion'))
        if opcion1==1:
            print("saludar")

        elif opcion1==2:
           break
    if opcion==2:
        break
print('saliendo del programa....')        




    