import datetime
import os

def renome():
    print("Bem-vindo(a) ao renomeador automático. Forneça as informações exigidas.\n")
    data_hoje = datetime.datetime.now().strftime("%Y-%m-%d")
    caminho = input('Digite o caminho da pasta: ')
    prefixo = input('Forneça o préfixo: ')
    extensao = input('Forneça a extensão: ')
    contador = 1
    contador_de_finalização = 0
    arquivos = os.listdir(caminho)

    for nome in arquivos:
        if nome.endswith(extensao):
            novo_nome = f'{prefixo}_{data_hoje}_{contador:03d}{extensao}'
            antigo_full = os.path.join(caminho, nome)
            novo_full = os.path.join(caminho, novo_nome)
            os.rename(antigo_full, novo_full)
            contador += 1
            contador_de_finalização +=1
            print(f'O processo foi finalizado {contador_de_finalização} vez(es)')
    print(f'Foram renomeados {contador_de_finalização} arquivos com exito.')
renome()