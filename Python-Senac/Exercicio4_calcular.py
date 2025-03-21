#leitura do nome e do salario de um funcionario
#vamos aprenser o nome e o salario do funcionario
#reajustar o salario em 50%

nome = input("Informe seu nome:")
salario = float(input("Informe seu salário:"))

novo_salario = salario * 1.5
#novo_salario = salario + (salario * 0.5)
#novo_salario = salario + (salario * 50 / 100)

print("Nome:",nome)
print("Salário:",salario)
print("Novo Salário:",novo_salario)