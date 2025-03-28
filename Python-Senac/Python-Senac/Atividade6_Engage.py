# Escreva um algoritmo que leia vários números positivos, parar a leitura quando for informado o número 0. Após o termino exibir:
    
# a. A quantidade de números lidos
# b. A média aritmética dos números lidos

y = 0
z = 0
x = int(input("Informe um número:"))
while x > 0:
    y = x + y
    z = z + 1
    
    x = int(input("Informe um número:"))
    #Digite "0" para "SAIR"

print("Quantidade de vezes perguntadas:",z)
print("A quantidade de números lidos",y)
print("A média artméticas dos números lidos", y / z)