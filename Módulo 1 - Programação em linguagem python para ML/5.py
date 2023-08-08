
# Escreva uma função que receba uma lista de números e retorne outra lista com os numeros ímpares

def getOdd(values: list):
    odd = []
    for value in values:
        if value % 2 != 0:
            odd.append(value)
    
    return odd


print(getOdd([0,1,2,3,4,5,6,7,8,9,10]))