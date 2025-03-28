#programa que calcula um abastecimento de combustivel com função de realizar desconto dependendo da quantidade de computivel comprado.

#valores da gasolina
alcool = 4.3
gasolina = 6.4
diesel = 6.1

combustivel = input("Informe o combustivel:\n[A] Alcool\n[G] Gasolina\n[D] Dielse\n")

if combustivel == "A":
    litros = float(input("Informe a quantidade de litros:"))
    if litros <= 20:
        print("Total a pagar:", litros * alcool)
        desconto = litros * 0.03
        print("Total a pagar com desconto:",litros * alcool - desconto)
    else:
        print("Total a pagar:", litros * alcool)
        desconto = litros * 0.05
        print("Total a pagar com desconto:",litros * alcool - desconto)

elif combustivel == "G":
    litros = int(input("Informe a quantidade de litros:"))
    if litros <= 20:
        print("Total a pagar:", litros * gasolina)
        desconto = litros * 0.03
        print("Total a pagar com desconto:",litros * gasolina - desconto)
    else:
        print("Total a pagar:", litros * gasolina)
        desconto = litros * 0.05
        print("Total a pagar com desconto:",litros * gasolina - desconto)

elif combustivel == "D":
    litros = int(input("Informe a quantidade de litros:"))
    if litros <= 20:
        print("Total a pagar:", litros * diesel)
        desconto = litros * 0.03
        print("Total a pagar com desconto:",litros * diesel - desconto)
    else:
        print("Total a pagar:", litros * diesel)
        desconto = litros * 0.05
        print("Total a pagar com desconto:",litros * diesel - desconto)
