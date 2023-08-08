
# Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes

def isPrimo(num):

    if num <= 1:
        return False
    
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True


def getPrimos(lista: list):
    primos = []
    for num in lista:
        if isPrimo(num):
            primos.append(num)
    
    return primos


print(getPrimos(range(0,100)))