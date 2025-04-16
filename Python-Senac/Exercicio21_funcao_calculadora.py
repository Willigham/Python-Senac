#realizando uma soma de dois numeros

 #criando a função para SOMAR
def somar(x, y):
    return  x + y

#criando a função para SUBTRAIR
def subtrair(x, y):
    return x - y

#criando a função para MULTIPLICAR
def multiplicacao(x, y):
    return x * y

#criando a função para DIVIDIR
def divisao(x, y):
    return x / y

#recebendo o tipo de operação
operacao = input("Qual operação você deseja fazer? ( '+'  '-'  '*'  '/' )")

if operacao == "+" and operacao =="-" and operacao =="*" and operacao =="/":

    a = float(input("Informe o numero 1:"))
    b = float(input("Informe o numero 2:"))

    if operacao == "+":
        print("SOMAR:",somar(a, b))

    elif operacao == "-":
        print("SUBITRAÇÃO:",subtrair(a, b))

    elif operacao == "*":
        print("MULTIPLICAÇÃO:",multiplicacao(a, b))

    elif operacao == "/":
        print("DIVISÃO:",divisao(a, b))

else:
    print("Operação inválida!")


