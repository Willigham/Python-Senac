#programa que calcula a media de um aluno
n1 = int(input("Informe a nota 1:"))
n2 = int(input("Informe a nota 2:"))
media = (n1 * 2 + n2 * 3) / 5
if media >= 6:
    print("Aluno Aprovaddo")
elif media < 2:
    print("Aluno Reprovado")
else:
    nova_nota = int(input("Informe a nova nota:"))
    if nova_nota >= 5:
        print("Aprovado em Recuperação")
    else:
        print("Reprovado em Recuperação")
