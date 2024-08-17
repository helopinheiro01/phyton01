import os
os.system("cls")

rest1 = float(input("Digite o valor da resistencia"))
rest2 = float(input("Digite o valor da resistencia"))
rest3 = float(input("Digite o valor da resistencia"))
rest4 = float(input("Digite o valor da resistencia"))

RE = (rest1 + rest2 + rest3 + rest4)
if (rest1 > rest2 and rest1 > rest3 and rest1 > rest4):
    maior = rest1
else:
    menor = rest1
if (rest2 > rest1 and rest2 > rest3 and rest1 > rest4):
    maior = rest2
else:
    menor = rest2
if (rest3 > rest1 and rest3> rest2 and rest3 > rest4):
    maior = rest3
else:
    menor = rest3
if (rest4 > rest1 and rest4 > rest2 and rest4 > rest3):
    maior = rest4
else:
    menor = rest4

print (input(f"Resistenia Equivalente {RE}"))
print (input(f"Maior resistencia: {maior}"))
print (input(f"Menor resistencia: {menor}"))