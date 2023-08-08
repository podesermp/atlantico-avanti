
# Dada uma lista contendo números inteiros, como você encontraria o maior número e o menos número dessa lista em uma única passagem?
# -> Orderaria a lista com o sorted() e para pegar o maior usaria o índice -1 e para pegar o menor usaria o 0, como na função maiorMenorSorted. Outra forma de fazer seria percorrer a lista e utilizar variaveis para ir armazenando o valor menos e o maior da iteração, como na função maiorMenorVariavel.


def maiorMenorSorted(lista:list):
    listaOrdenada = sorted(lista)
    maior = listaOrdenada[-1]
    menor = listaOrdenada[0]
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")



def maiorMenorVariavel(lista:list):
    menor = lista[0]
    maior = lista[0]
    for obj in lista[1:]:
        if obj < menor:
            menor = obj
        if obj > maior:
            maior = obj
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")



lista = [1,6,7,3,10,5,15,9,11]

maiorMenorSorted(lista)
maiorMenorVariavel(lista)