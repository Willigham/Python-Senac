#Recebendo dados Altura e Peso
# peso = float(input("Informe seu peso:"))
# altura = float(input("Informe sua altura:"))
# sexo = input("Informe seu sexo: [M/F]")

#Função de IMC

def Calcular_IMC(peso, altura):
    imc = peso / (altura ** 2)
    print("IMC:", imc)
    if(imc < 18.5):
        print("Abaixo do peso")
    elif(imc > 25):
        print("Acima do peso")
    else:
        print("Peso normal")
    

def peso_ideal(sexo, altura):
    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
        print("Peso ideal:", peso_ideal)
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
        print("Peso ideal:", peso_ideal)
    else:
        print("Sexo invalido")


