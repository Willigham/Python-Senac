
frutas = ["Banana", "Maçã", "Uva", "Goiaba", "Manga"]
frutas.append("Pitomba")
print(frutas) #exibir toda lista
print(frutas[1]) #exibe um indice expecifico "Exemplo [1] = Maçã"
print(frutas[-1]) #exibe o ultimo elemento da lista
print(frutas[2:4]) #exibe o intervalo, posição 2 até 3
print(frutas[2:]) #exibe a partir da posição 2
print(frutas[:4]) #exibe até a posição 3

# percorrer a lista
for i in frutas: #exibe cada item da lista
    print(i)

#percorrer a lista
for i in range(len(frutas)): #exibe o tamanho da minha lista 0 até 5 = total 6 itens
    print(i + 1 ,frutas[i]) #"i + 1" vai exibir a lista começando pelo 1 até o numero 6 ou a quantidades de itens.

