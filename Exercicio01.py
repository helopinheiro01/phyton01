import os
os.system("cls")

n = input("Digite o nome de um produto: ")
valor = int(input("Digite o valor do produto:"))
if (valor >= 50 and valor <200):
    desconto = valor - valor * 0.05
if(valor >= 200 and valor <500):
    desconto = valor - valor * 0.06
if (valor >= 500 and valor <1000):
    desconto = valor - valor * 0.07
if (valor >=1000):
    desconto = valor - valor * 0.08
if (valor <= 0):
    desconto = 0
print(f"Nome: {n}")
print(f"Valor: {valor}")
print(f"Desconto: {desconto}")

