import os
import shutil
import tkinter as tk

def organizar():
    
    janela = tk
    
    caminho = input("Digite o caminho da pasta: ")
    categorias = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".doc", ".py"],
        "Vídeos": [".mp4", ".mkv", ".mov", ".avi"],
        "Musicas": [".mp3", ".wav", ".flac"],
        "Compactados": [".zip", ".rar", ".7z"]
    }

    arquivos = os.listdir(caminho)

    for nome_arq in arquivos:
        caminho_full = os.path.join(caminho, nome_arq)
    
        if os.path.isfile(caminho_full):
            nome_base, extensao = os.path.splitext(nome_arq)
            extensao = extensao.lower()
            movido = False

            for nome_da_pasta, lista_ext in categorias.items():
                if extensao in lista_ext:
                    caminho_novo = os.path.join(caminho, nome_da_pasta)
                    
                    if not os.path.exists(caminho_novo):
                        os.makedirs(caminho_novo)
                    
                    destino_final = os.path.join(caminho_novo, nome_arq)
                    shutil.move(caminho_full, destino_final)
                    movido = True
                    break
organizar()