def decimal_binario(n):
    restos = []
    while n > 0:
        restos.append(str(n%2))
        n = n // 2
    restos.reverse()
    return ''.join(restos)

def binario_decimal(cadena_binaria):
    decimal = 0
    potencia = len(cadena_binaria) - 1
    for bit in cadena_binaria:
        decimal += int(bit) * (2 ** potencia)
        potencia -= 1
    return decimal