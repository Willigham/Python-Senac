
#crie uma função que recebe uma lista como parametro, a lista vai contar notas de alunos, a função deve calcular a média dos valores e retornar essa informação



def media(a, b):
    return a / b

quant = int(input("Quantidade de alunos: "))

notas = []
for i in range(quant):
    notas.append(int(input("Informe a nota: ")))

soma = sum(notas)
print("1 A media notas:",media(soma, quant))

# ou

def media(lista):
    media = sum(lista) / len(lista)
    return media

print("2 A media notas:",media(notas))