# QUESTÃO DA PROVA MOD 3
''' def contar_e_somar_positivos(numeros):
    quantidade_positivos = 0
    soma_positivos = 0
    for numero in numeros:
        if int(numero) > 0:
            quantidade_positivos += 1
            soma_positivos += int(numero)
    return quantidade_positivos, soma_positivos

def main():
    sequencia = input('').split()
    quantidade_positivos, soma_positivos = contar_e_somar_positivos(sequencia)
    print("Número de positivos lidos:", quantidade_positivos)
    print("Soma dos números positivos:", soma_positivos)

if __name__ == "__main__":
    main()
'''

# LOOP COM ERRO PARA ENTENDER DEBUG
'''def h(n):
    print('Start h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

f(2)'''

# AULA DE DEPURAÇÃO
"""def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n-1)

def fatorial_iterativo(n):
    fat = n
    i = n-1
    while i >= 1:
        fat *= i
        i -= 1

    return fat

número = 5

print ('O fatorial de {} é {} - método recursivo'.format(número, fatorial_recursivo(número)))

print ('O fatorial de {} é {} - método iterativo'.format(número, fatorial_iterativo(número)))"""

n = 5
def umsimpleslaco( n ):
    resultado = 1 / n
    while n > 0:
        print("Estou aqui")
        n = n + 1
    return resultado

