#propragama que realiza uma pequena eleição e exibe o resultado da eleição
codigo = 1
joao, simone, nulo = 0

while codigo != 0:
    codigo = int(input("VOTE:\n[1] JOÃO\n[2] SIMONE\n[9] NULO\n"))
    if codigo != 0:
        if codigo == 1:
            joao += 1
        elif codigo == 2:
            simone += 1
        elif codigo == 9:
            nulo += 1
        else:
            print("VOTO INVÁLIDO")
print("Votos de JOÃO:",joao)
print("Votos de SIMONE:",simone)
print("Votos NULOS:",nulo)