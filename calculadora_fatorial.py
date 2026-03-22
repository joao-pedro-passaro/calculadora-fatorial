#Calculadora Fatorial:

numero = int(input("Digite o número:"))
fatorial = 1
contador = 1
while contador <= numero:
    fatorial *= contador
    contador += 1
print (f"{numero}! = {fatorial}")

