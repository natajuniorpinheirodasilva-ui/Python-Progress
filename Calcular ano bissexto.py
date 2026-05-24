print("Cálculador de ano bissexto")

def calculo():
    ano = int(input(("\nAno: ")))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Ano bissexto")
    else:
        print("Ano normalzera")
calculo()