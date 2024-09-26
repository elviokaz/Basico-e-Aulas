'''EXEMPLO FATORIAL'''
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)



'''DIGITAR UM NÚMERO POSITIVO'''

'''num = eval(input('Digite um número positivo:'))
while num < 0:
    num = eval(input('Digite um número positivo:'))'''

'''ARMAZENAR NOMES E ARMAZENAR EM UMA LISTA'''

'''l = []
nome = input('Digite um nome:')
while nome != '':
    l.append(nome)
    nome = input('Digite um nome:')

for i in l:
    print(i)'''