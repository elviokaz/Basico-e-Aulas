def eh_palindromo(numero):
    # Convertemos o número para uma string para facilitar a manipulação
    numero_str = str(numero)

    # Verificamos se a string é igual à sua reversão
    if numero_str == numero_str[::-1]:
        return "sim"
    else:
        return "não"


# Leitura do número natural da entrada bem básico, para texto preencher o input
numero = int(input())

# Verificação se o número é palíndromo
resultado = eh_palindromo(numero)

# Impressão do resultado
print(resultado)