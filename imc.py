import os
os.system("cls")

def imc(peso,altura):
    return peso/(pow(altura,2))
def soma(nome):
    try:
        return int(input(f"Informe {nome}:"))
    except:
            print ("Valor Invalido")
            return soma()
os.system("cls")
c = "s"
while c == "s" or c == "S":
     os.system("cls")
     peso = soma("Peso: ")
     altura = soma("Altura: ")

     print (imc(peso,altura))
     c = input("Deseja continuar?")
