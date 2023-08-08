
## Escreva um prgrama que leia números digitados pelo usuário e pare quando o número 0 for digitado. No final, imprima a média dos números digitados

# indice = 1
# aux = int(input(f"Valor ({indice}): "))
# acumulate = aux

# while (aux != 0):
#     indice += 1
#     aux = int(input(f"Valor ({indice}): "))
#     acumulate += aux

# print(f"Média: {acumulate/(indice-1)}")


values = []
aux = int(input("Valor: "))
while (aux != 0):
    values.append(aux)
    aux = int(input("Valor: "))

if len(values) == 0:
    print("Insira valores para realizar a divisão")
else:
    print(sum(values)/len(values))