# Escreva um algoritmo que calcule o prêmio para um nadador de acordo com a distância percorrida. Se o nadador percorrer uma distância menor que 800 metros, recebe R$ 5.000,00 reais de prêmio. Caso percorra uma distância entre 800 e 1500 metros, recebe R$ 10.000,00. E se percorrer uma distância superior a 1500 metros, recebe R$ 15.000,00 em prêmio. Escreva um algoritmo que leia a distância percorrida e mostre na tela o valor da premiação a ser recebida pelo nadador.

distancia = int(input("Informe a distancia percorrida: "))

if(distancia < 800):
    print("Seu prêmio é de R$ 5.000,00")
elif(distancia <= 1500):
    print("Seu prêmio é de R$ 10.000,00")
else:
    print("Seu prêmio é de R$ 15.000,00")