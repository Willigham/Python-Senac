#Recebendo dados Altura e Peso
peso = float(input("Informe seu peso:"))
altura = float(input("Informe sua altura:"))

#Calculo de IMC
imc = peso / (altura * altura)

#Esctrutura se e senão em Python:
if(imc < 19.5):
    print("Abaixo do peso")
elif(imc > 25):
    print("Acima do peso")
else:
    print("Peso normal")
