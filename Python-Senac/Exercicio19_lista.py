
#lista
num = [2, 4, 3, 10, 5, 7, 1, 9, 6, 8]

# num = []
# for i in range(10):
#     num.append(int(input("Infome o numero: ")))

print("SUA LISTA:", num)

print("\n----------------------------------")
print("#o elemtento da posição 5")
print(num[5]) 

print("\n----------------------------------")
print("#intervalo da posição 0 até 5")
print(num [:5]) 

print("\n----------------------------------")
print("#Intervalo da posição 5 até 9")
print(num[5:9]) 

print("\n----------------------------------")
print("#A soma do todos os elementos.")
print(sum(num)) 

print("\n----------------------------------")
print("#A media de todos os elementos")
print(sum(num) / 10) 

print("\n----------------------------------")
print("#Apenas os numeros pares.")
for i in range(len(num)):
    if num[i]%2 == 1:
        print(i)

print("\n----------------------------------")
print("#Apresentar os elementos da lista, um embaixo do outro.")
for i in num: 
    print(i)

print("\n----------------------------------")
print("#Apresentar a lista toda, a posição e o valor, Ex: [0] -> 2.")
for i in range(len(num)):
    print("indice",i, "->", num[i])

print("\n----------------------------------")
print("#Ordena e apresentar a lista ordenada.")
num.sort() 
print(num,"\n")





