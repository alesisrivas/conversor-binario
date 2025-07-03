from conversor import decimal_binario,binario_decimal

def mostrar_menu():
    print("\nConversor Binario")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-3): ")

        if opcion == "1":
            numero = int(input("Ingresa un numero decimal: "))
            resultado = decimal_binario(numero)
            print(f"Resultado: {resultado}")
        
        elif opcion == "2":
            binario = input("Ingresa un numero Binario: ")
            resultado = binario_decimal(numero)
            print(f"El resultado a decimal es: {resultado}")

        elif opcion == "3":
            print("¡Hasta Luego!")
            break
        else:
            print("Opcion invañoda, elegi una correcta entre 1,2 o 3.")

    if __name__ == "__main__":
        main()