#programa que mostre o conceito relativo á nota. (A, B, C, D e E)

nota = int(input("Informe a nota:"))
if nota < 2:
    print("Conceito E")
elif nota < 4:
    print("Conceito D")
elif nota < 6:
    print("Conceito C")
elif nota < 8:
    print("Conceito B")    
else:
    print("Conceito A")