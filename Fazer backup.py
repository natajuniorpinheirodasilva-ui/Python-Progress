import shutil
import datetime
import os

def auto():
        
    while True:
        try:
            print(f"Diretório atual: {os.getcwd()}. Só será encontrado arquivos nesse diretório.\n")
            data = input("Forneça o nome do arquivo com sua extensão. (Ex: teste.txt): ")
            r = input("Quer reiniciar o programa? Y e N: ").lower()
            
            if not os.path.exists(data):
                print(f"Erro, o arquivo {data} não existe no sistema.")
                
                while True:
                    if r == "y":
                        continue
                    if r == "n":
                        break
                    if not r == ["y", "n"]:
                        print("Não foi fornecido Y ou N")
                        continue
                
            
            if os.path.exists(data):
                data_hoje = datetime.date.today().strftime("%Y-%m-%d-%H-%M")
                nome_base, extensao = os.path.splitext(data)
                nome_back = f"{nome_base}_backup_{data_hoje}{extensao}"

                shutil.copy2(data, nome_back)

                print("O backup do arquivo foi criado.")
                print(f"Arquivo original: {data}")
                print(f"Novo arquivo: {nome_back}")

        except FileNotFoundError:
            print("Erro, arquivo não existente.")
            continue
        except PermissionError:
            print("Erro de permissão.")
            continue
        except Exception as e:
            print(f"Erro de {e}")
            break

auto()