
# Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética

def sort(lista:list):
    return sorted(lista, key=lambda x: x[0])


lista = [
    ('Marcos', 24),
    ('Sara', 17),
    ('Paulo', 21),
    ('Batista', 41),
    ('Antônio', 12),
    ('Juliana', 23),
    ('César', 23),
]

print(sort(lista))


