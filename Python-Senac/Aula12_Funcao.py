#criando função
def linha():
    print("-------------------------")

def calcular(n1, n2):
    m = n1 + n2 / 2
    return m
    #return n1 + n2 / 2


#chamando a função "linha()"
linha()
print("  C A L C U L A D O R A  ")
linha()
a = float(input("Informe a nota 1: "))
b = float(input("Informe a nota 2: "))
media = calcular(a, b)
#media = (a+b)/2
print("média:", media)
linha()