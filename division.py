def div(num_1, num_2):
    try:
        result = num_1 / num_2
        print(f'{num_1} / {num_2} es igual a {result}')
    except ZeroDivisionError:
        result = "Operación inválida: No se puede dividir por cero"
        print(result)
    return result