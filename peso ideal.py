sexo = input("Digite h para homens e m para mulheres: ")
altura = input("Digite sua altura: ")

alt = eval(altura)

if sexo == 'h':
    peso = (72.7 * alt) - 58
else:
    peso = (62.1 * alt) - 44.7

print('O peso ideal é', peso)