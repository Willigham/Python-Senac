
curso = ["Informática Básica", "Excel", "Programador", "Manutenção de Computadores"]

valor = [150, 200, 500, 400]

print("\n------------------------------")
#Apresente todos os cursos com o seu valor ao lado.
for i in range(len(curso)):
    print(curso[i], "-", valor[i])

print("\n------------------------------")
#apresente o nomes apenas dos valores maiores que 300
for c, v in zip(curso, valor):
    if v > 300:
        print(c)

print("\n------------------------------")
#apresente o nome do curso com o valor maior
maior_valor = max(valor) #retorna o maior valor -> 500
indice = valor.index(max(valor))
print("maior valor:", curso[indice])
#print("maior valor:", curso[valor.index(max(valor))])  #diminuir o codigo

print("\n------------------------------")
#apresente o nome do curso com o valor menor
menor_valor = min(valor) #retorna o menor valor -> 150
indice = valor.index(menor_valor)
print("Menor valor:", curso[indice])

print("\n------------------------------")
#Calcule a média dos valores dos cursos e apresente
media = sum(valor) / len(valor)
print("Media dos valores:", media)

print("\n------------------------------")
#Aprensete os cursos com valores menores que a média
print("Menores que a média")
for c, v in zip(curso, valor):
    if v < media:
        print(c)







