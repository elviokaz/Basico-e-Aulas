'''COMANDO FOR // só rodar ou jogar no console '''

'''I = ['cão', 'gato', 'coelho']
for i in I:
    print(i)'''

'''s = 'algoritmos'
for c in s:
    if c in 'aeiou':
        print(c)'''

'''COMANDO RANGE()'''

'''for x in range(10):
    print(x)

for y in range(1, 20, 2):
    print(y)'''

'''k = ['a', 'b', 'c']
for i in range(len(k)):
    print(k[i])'''
'''desse jeito a fórmula printa tudo que estiver na lista(array)'''

'''// ACUMULADORES //'''

'''acum = 0
for x in range(1, 101):
    if x % 2 == 0:
        acum = acum + x
print(acum)'''

'''// LOOPs ANINHADOS'''

str_list = ['João', 'Roberto', 'Rafael']

for  nome in str_list:
    for c in nome:
        if c in 'aeiou':
            print(c)