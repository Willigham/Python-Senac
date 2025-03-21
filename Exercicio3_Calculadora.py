
#Criando Calculadora com metodo de repetição
sair = 0
while sair < 2:
    print("======================")
    print("====  CACULADORA  ====")
    print("======================")
    a = int(input("Informe um numero: "))
    b = int(input("Informe outro numero:"))
    print("digite um numero para:")
    x = int(input("[1] SOMAR\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[4] DUVIDIR\n"))

    #Operadores aritmeticos em Python:
    if(x == 1):
        print("A Soma é:",a + b)
    elif(x == 2):
        print("A Subtração é:",a - b)
    elif(x == 3):
        print("A Multiplicação é:",a * b)
    elif(x == 4):
        print("A Divisão é:",a / b)
    sair = int(input("[1] RETORNAR | [2] SAIR\n"))