from addition import add
from substraction import sub
from multiplication import mult
from division import div
from potentiation import pot
from module import mod

def game():
    score = 0
    
    while True:
        print('\n======== Menú ========'
              '\n1. Suma'
              '\n2. Resta'
              '\n3. Multiplicación'
              '\n4. División'
              '\n5. Potenciación'
              '\n6. Módulo'
              '\n0. Salir')
        option = int(input('\nElige una opción: '))

        if option == 0:
            break

        num_1 = int(input('Ingresa el primer número: '))
        num_2 = int(input('Ingresa el segundo número: '))
        answer = int(input('Tu respuesta: '))
        
        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')
        elif option == 2:
            result = sub(num_1, num_2)
            if result == answer:
                score += 1
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')
        elif option == 3:
            result = mult(num_1, num_2)
            if result == answer:
                score += 2
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')
        elif option == 4:
            result = div(num_1, num_2)
            if result == answer:
                score += 2
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')
        elif option == 5:
            result = pot(num_1, num_2)
            if result == answer:
                score += 4
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')
        elif option == 6:
            result = mod(num_1, num_2)
            if result == answer:
                score += 4
                print('¡¡Correcto!!')
            else:
                print('Incorrecto')


    print(f'======== Game Over ========'
          f'\nTu puntaje final es {score}'
          '\n¡No te rindas!\n')
game()