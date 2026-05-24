def tabuada():
    while True:
        try:
            tab = int(input("Forneça um número de 1 a 50 e veja sua tabuada: "))

            if 1 <= tab <= 50:
                print(f"\nTabuada do {tab}\n")

                for i in range(1, 11):
                    print(f"{tab} x {i} = {tab * i}")

                break
            else:
                print("Porra, tá escrito de 1 a 50 carai.\n")

        except ValueError:
            print("Digita um número válido.\n")

    print("\nIsso aí dog, já viu a tabuada.")
tabuada()

def vogais():
    frase = input("Digite uma frase: ").lower()

    vogais = "aeiou"
    contador = 0

    for letra in frase:
        if letra in vogais:
            contador += 1

    print(f"A frase tem {contador} vogais.")
vogais()

def jogo_adivinhacao():
    import random
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Eu pensei em um número entre 1 e 100. Tente adivinhar!\n")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        palpite_str = input("Digite seu palpite: ")
        
        try:
            palpite = int(palpite_str)
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"\nParabéns! Você acertou o número {numero_secreto}!")
                print(f"Você usou {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            else:
                print("Muito alto! Tente um número menor.")

        except ValueError:
            print("Por favor, digite apenas números inteiros!")
jogo_adivinhacao()