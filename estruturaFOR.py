numero = int(input("Digite um número positivo:"))
while numero != 0:
    if numero > 2 and numero % 2 == 0:
        print("O número", numero, "não é primo.")

    else:
        contador = 0
        for i in range(1, numero + 1, 1):
            if numero % i == 0:
                contador = contador + 1
            if contador == 2:
                print("O número", numero, "é primo.")
            else:
                print("O número", numero, "não é primo.")
    numero = int(input("Digite um número positivo:"))