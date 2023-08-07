# Escreva um programa que solicite ao usuário uma palçavra e verifique se ela é um palíndromo

from time import sleep


def isPalindromo(w: str):
    if w.lower() == w[::-1].lower():
        return True
    return False


word = input("Insira uma palavra: ")


if isPalindromo(word):
    print("É palíndromo")
else:
    print("Não é palíndromo")