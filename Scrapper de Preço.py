import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

def web_scrapper():
    
    while True:            
       
        try:    
            
            response = requests.get("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
            
            if response.status_code == 200:
                
                print("Resposta obtida com sucesso. Começando o Scrapping")

                var = BeautifulSoup(response.text, "html.parser").find("p", class_="price_color")
                print(var.text)
                
                if os.path.exists("log_precos.csv") == True:
                    with open("log_precos.csv", "a") as f:
                        csv.writer(f).writerow([f"Data: {datetime.now().strftime('%d-%m-%Y-%H-%M')}", f"Valor: {var.text}"])
                else:
                    with open("log_precos.csv", "w") as f:
                        csv.writer(f).writerow(["Data","Valor"])
                        csv.writer(f).writerow([datetime.now().strftime('%d-%m-%Y-%H-%M'), var.text])
                print(f"Valor e data salvos em {os.path.abspath("log_precos.csv")}")
                break
  
            else:
                print("Sem resposta")
                break
        except requests.exceptions.ConnectionError:
            print("Erro ao estabelecer conexão.")

web_scrapper()