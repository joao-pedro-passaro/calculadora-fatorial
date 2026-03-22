#Calculadora Fatorial:

numero = int(input("Digite o número:"))
fatorial = 1
contador = 1
while contador <= numero:
    fatorial *= contador
    contador += 1
print (f"{numero}! = {fatorial}")

#Explicação: numero é uma variável. int se refere que o que será escrito no input, devera ser um número inteiro.
#O input foi usado para que a você pudesse definir qual será o número int.
#fatorial e contador são variaveis de valor 1. Fatorial é igual a 1 porque no fatorial se começa multiplicando por 1. Contador igual a 1 porque ele começara no 1 e vai ate o número escolhido.
#while= Enquanto contador (1) for menor ou igual ao numero (variável da sua escolha) ele irá repetir os valores.
#Por exemplo, se o número escolhido for 5, ele vai se repetir 5x, na 6x ele para.
#o valor de fatorial é igual ao seu valor multiplicando sempre o valor do contador. Se contador é igual a 1 vai ser 1*1. Se contador é igual a 6 vai ser 1*6.
#o valor de fatorial muda porque ele é igual seu resultado.
#contador += 1 vai sempre adicionar o múmero 1 ao contador.
#print simplesmente colocou o numero incial ao lado de "!" = fatorial.


