import Exercicio25_FuncaoIMC

def menu():
    print("-"*20)
    print("-- Academia Kalango --")
    print("-- MENU --")
    print("1 - IMC")
    print("2 - Peso Ideal")
    print("9 - Sair")
    print("-"*20)

def menu_imc():
    altura = float(input("Informe a altura: "))
    peso = float(input("Informe o peso: "))
    Exercicio25_FuncaoIMC.Calcular_IMC(peso, altura)

def menu_peso():
    sexo = input("Informe o sexo (M ou F): ")
    altura = float(input("Informe a altura: "))
    Exercicio25_FuncaoIMC.peso_ideal(sexo, altura)

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        menu_imc()
    elif opcao == 2:
        menu_peso()
    elif opcao == 9:
        break #encerrar while
    else:
        print("Opção inválida")