import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def IO():
    while True:
        try:
            n1 = float(input("Forneça o n1: "))
            n2 = float(input("Forneça o n2: "))
            op = int(input(
                "Qual será a operação?\n"
                "1 -> +\n"
                "2 -> -\n"
                "3 -> *\n"
                "4 -> /\n"
                "--------\n"
            ))
            limpar_tela()
            
            match op:
                case 1:
                    print(f"Foi escolhido soma: {n1} + {n2} = {n1 + n2}\n")
                case 2:
                    print(f"Foi escolhido subtração: {n1} - {n2} = {n1 - n2}\n") 
                case 3:
                    print(f"Foi escolhido multiplicação: {n1} * {n2} = {n1 * n2}\n")
                case 4:
                    print(f"Foi escolhido divisão: {n1} / {n2} = {n1 / n2}\n")
                case _:
                    print("Não foi fornecido um número válido.\n1")
                    continue 

        except ValueError:
            print("Erro de valor ocorrido, forneça um número")
            continue 
        except ZeroDivisionError:
            print("Porra, não da pra dividir por zero filho da puta.")
            continue 

        while True:
            quer = input("Quer fazer outra conta? S/N: ").lower().strip()
            if quer in ('s', 'sim'):
                break
            elif quer in ('n', 'não', 'nao'):
                print("Valeu, até mais!")
                return
            else:
                print("Não foi fornecido S nem N, tente novamente.")
                
IO()