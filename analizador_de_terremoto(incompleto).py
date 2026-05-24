import sys
import requests
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup


class Extrator:
    def de_imagem(self, caminho):
        try:
            imagem = Image.open(caminho)
            return pytesseract.image_to_string(imagem)
        except Exception as e:
            print("Erro ao abrir imagem:", e)
            return ""

    def de_url(self, url):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")
            return soup.get_text()
        except Exception as e:
            print("Erro ao acessar URL:", e)
            return ""

    def de_texto(self, texto):
        return texto


class Analisador:
    def __init__(self):
        self.points = 100

    def analisar(self, texto):
        if texto.count("!") > 3:
            self.points -= 2
        return self.points


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("python main.py imagem <caminho>")
        print("python main.py url <link>")
        print("python main.py texto <seu_texto>")
        return

    tipo = sys.argv[1]
    entrada = " ".join(sys.argv[2:])

    extrator = Extrator()

    if tipo == "imagem":
        texto = extrator.de_imagem(entrada)
    elif tipo == "url":
        texto = extrator.de_url(entrada)
    elif tipo == "texto":
        texto = extrator.de_texto(entrada)
    else:
        print("Tipo inválido")
        return

    print("\nTexto extraído:\n")
    print(texto[:500])  # limita saída

    analisador = Analisador()
    pontos = analisador.analisar(texto)

    print("\nPontuação:", pontos)


if __name__ == "__main__":
    main()
