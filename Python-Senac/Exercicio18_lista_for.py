#criando variavel "Alunos" onde vai receber uma lista de pessoas
alunos = []
notas = []
notaFinal = []
#essa variavel será usada para servir de numero de repetição do laço for
quant = int(input("Quantos alunos voce quer? "))


 #criando "Repetição for" que receberá nomes de 5 alunos
for i in range(quant):
    alunos.append(input("Informe o nome do aluno: "))
    notas.append(float(input("Informe a nota desse aluno: ")))
    if notas[i] > 5:
        notaFinal.append("Aprovado") 
    else:
        notaFinal.append("Reprovado")

#exibindo o nome e nota dos alunos
for i in range(quant):
    print(alunos[i], "-", notas[i], "-", notaFinal[i])