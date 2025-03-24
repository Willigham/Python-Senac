#Escreva um algoritmo que leia dois numeros, e escreva os números entre o intervalo deles.

x = int(input("Informe o primeiro numero:"))
y = int(input("Informe o segundo numero:"))

for a in range(x, y+1):
    print(a)