

# Escreva uma função que receba duas lista e retorne outra lista com elementos que estão presentes em apenas uma das listas

def differenceList(list1:list, list2:list):
    dif1 = set(list1).difference(set(list2))
    dif2 = set(list2).difference(set(list1))
   
    return sorted(list(dif1.union(dif2)))


print(differenceList([1,6,12,18,24,36,42,49,54,60], [1,9,18,27,36,45,54,63,72,81,90]))