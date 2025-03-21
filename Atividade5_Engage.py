#- Escreva um algoritmo que calcule o salário de funcionários de uma empresa. O salário é composto do vencimento base de 1600, acrescido de uma gratificação de escolaridade definida pela seguinte tabela:

#"base" será o valor base do salario, variavel valor1 até valor4 receberá o valores diferente.
base = 1600
valor1 = 500
valor2 = 700
valor3 = 800
valor4 = 100

nome = input("Informe seu nome: ")
escolaridade = int(input("Informe sua escolaridade:"))
if(escolaridade == 1):
    print(nome, "seu sário será:", base + valor1)
elif(escolaridade == 2):
    print(nome, "seu sário será:", base + valor2)
elif(escolaridade == 3):
    print(nome, "seu sário será:", base + valor3)
else:
    print(nome, "seu sário será:", base + valor4)