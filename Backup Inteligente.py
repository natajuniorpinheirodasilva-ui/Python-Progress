import zipfile
import time
import os
from datetime import datetime

tempo_agora = time.time()
limite_segundos = 7 * 86400
contador = 0
contador2 = 0
caminho = input('Forneça o caminho da pasta: ')
nome_zip = f"backup_{datetime.now().strftime('%Y-%m-%d')}.zip"

arquivos = os.listdir(caminho)

with zipfile.ZipFile(nome_zip, 'w') as meu_zip:
    
    for nome_arq in arquivos:  
        caminho_full = os.path.join(caminho, nome_arq)
        tempo_arquivo = os.path.getmtime(caminho_full)
    
        if os.path.isfile(caminho_full):
            tempo_arquivo = os.path.getmtime(caminho_full)

            if (tempo_agora - tempo_arquivo) < limite_segundos:
                        meu_zip.write(caminho_full, nome_arq)
                        print(f'Arquivo {nome_arq} adicionado ao backup')
                        contador += 1
                        contador2 += 1
                        print(f'{contador} adicionado')
print(f'Foram adicionado(s) {contador2} arquivo(s) ao zip.')