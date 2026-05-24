def conversor():
    while True:
        conversao = input("Digite 1 para Célsius -> Fahrenheit. 2 para Fahrenheit -> Célsius: ")
        
        if conversao == "1":
            grauf = float(input("°F: "))
            calculof = (grauf-32) / 1.8
            print(f"{grauf}°F convertido(s) para Célsius fica: {calculof}°C")
            break
        elif conversao == "2":
            grau = float((input("°C: ")))
            calculo = grau*1.8+32
            print(f"{grau}°C convertido(s) para Fahrenheit fica: {calculo}°F")
            break
        else:
            print("Não digite outro número além de 1 e 2.")
            continue
    print("Obrigado por usar meu conversor motherfucker")
conversor()