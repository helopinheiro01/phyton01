import os
os.system("cls")

def inserir():
    return input("Digite um numero")

def pares(lista):
    pares = []
    for x in lista:
        if int (x)%2==0:
            pares.append(x)
    return pares
def impares(lista):
    impares = []
    for x in lista:
        if int (x)%2!=0:
            impares.append(x)
    return impares
def maior(lista):
    return max(lista)
def menor(lista):
    return min(lista)
def media(lista):
    aux = 0
    for x in lista:
        aux = aux + int(x)
    media = aux / len(lista)
    return media
 
entrada = inserir()
lista = entrada.split(",")

print(pares(lista))
print(maior(lista))
print(menor(lista))
print(media(lista))
