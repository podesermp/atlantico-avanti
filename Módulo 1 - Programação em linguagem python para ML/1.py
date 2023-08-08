

# Escreva um programa que solicite ao usuário uma palçavra e verifique se ela é um palíndromo

def isPalindromo(w: str):
    if w.lower() == w[::-1].lower():
        return True
    return False


word = input("Insira uma palavra: ")
print()

if isPalindromo(word):
    print("É palíndromo")
else:
    print("Não é palíndromo")