# Dada uma lista de strings ["banana", "maçã", "laranja", "abacaxi"] crie uma nova lista com as palavras que tem mais que 5 letras e outra lista com as palavras que terminam com a letra a


import unicodedata

lista = ["banana", "maçã", "laranja", "abacaxi"]

finishedA = []
greater5 = []

for obj in lista:
    word = ''.join(ch for ch in unicodedata.normalize('NFKD', obj) if not unicodedata.combining(ch))  #remover a acentuação da string
    if word[-1] == 'a':
        finishedA.append(obj)
    if len(word) > 5:
        greater5.append(obj)


print(f"Lista com palavras com mais de 5 letras: {greater5}")
print(f"Lista com palavras terminadas em 'a': {finishedA}")