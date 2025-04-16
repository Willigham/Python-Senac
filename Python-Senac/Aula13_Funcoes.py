import datetime

def exibir_msg(n):
    data_hora = datetime.datetime.now()
    hora = int(data_hora.strftime("%H"))
    if hora >= 6 and hora < 12:
        print("Bom dia", n)
    elif hora >= 12 and hora < 18:
        print("Boa tarde", n)
    elif hora >= 18 and hora < 23:
        print("Boa noite", n)
    elif hora >= 0 and hora < 6:
        print("Boa madrugada", n)
