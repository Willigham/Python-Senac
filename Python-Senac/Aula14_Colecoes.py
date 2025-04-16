#lista
#indexada, ordenada, pode ser modificada
lista = ["Joao", "Tiago", "Pedro"]
print(lista[0]) # acessando pela indice
lista.sort() # ordena a lista
lista[1] = "Maria" # modificando uma posição da lista

#tupla
#indexada, não ordenada, não pode ser moficiada
tupla = ("Joao", "Tiago", "Pedro")
print(tupla[0]) # acessando pela indice
# tupla.sort()
# tupla[1] = "Maria"

#conjunto
#não é indexada, não ordenada, não pode ser modificada
conj = {"Joao", "Tiago", "Pedro"}
print("Tiago" in conj) # retorna Verdadeir se estiver no conjunto

#dicionario
aluno = {"Nome": "Joao",
         "Idade": 44,
         "Telefone": "9999-1010"}

