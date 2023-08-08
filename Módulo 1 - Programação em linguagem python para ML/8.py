
# Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor da lista

def secBigger(lista: list):
    return sorted(lista)[-2]

lista = [1,6,7,3,10,5,15,9,11]
print(f"Segundo maior da lista {lista} é := {secBigger(lista)}")