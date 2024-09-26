def processa_sequencia(numeros):
    # Inicializa as variáveis para contar positivos e somar os positivos
    quantidade_positivos = 0
    soma_positivos = 0

    # Itera sobre a lista de números
    for num in numeros:
        if num > 0:
            quantidade_positivos += 1
            soma_positivos += num

    # Imprime os resultados no formato especificado
    print(f"Número de positivos lidos: {quantidade_positivos}")
    print(f"Soma dos números positivos: {soma_positivos}")


# Leitura da entrada
numero1, numero2, numero3, numero4 = map(int, input('').split())

# Cria uma lista com os números lidos
numeros = [numero1, numero2, numero3, numero4]

# Processa a sequência de números
processa_sequencia(numeros)