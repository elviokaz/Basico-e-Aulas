"""PROGRAMA PARA CADASTRAR PRODUTOS"""

def cadastrar_produtos():
    produtos = {}
    n = int(input("Quantidade de produtos a cadastrar: ")) #DEFINE QUANTOS PRODUTOS TERÁ A LISTA
    
    for _ in range(n):
        produto = input("Nome do produto: ").lower() #TIVE QUE PASSAR MINÚSCULO PARA EVITAR ERRO
        preco = float(input("Preço do produto: "))  #TRANSFORMAÇÃO EM FLOAT NECESSÁRIA PARA PYTHON
      """pediram pra não cadastrar o produto 2x"""
        if produto in produtos:
            print("Produto já cadastrado")
        else:
            produtos[produto] = preco
    
    return produtos

"""Finalização para retornar o preço de determinado produto"""
def buscar_preco(produtos):
    while True:
        produto = input("Digite o nome do produto (ou 'Fim' para encerrar): ").lower()
        if produto == 'fim':
            break
        elif produto in produtos:
            print("Preço de", produto.capitalize() + ":", produtos[produto])
        else:
            print("Produto não cadastrado")

# Função principal
def main():
    produtos = cadastrar_produtos()
    buscar_preco(produtos)

if __name__ == "__main__":
    main()
