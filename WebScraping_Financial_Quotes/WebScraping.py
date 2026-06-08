#Web Scraping simples: cotações de pares de moedas dólar Investing.com

import requests
from bs4 import BeautifulSoup
import random
import time

url = "https://br.investing.com/currencies/single-currency-crosses"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'} #Header facilita o acesso ao site, simulando um navegador

while True:
    espera = random.uniform(3,5)  # adicionar uma espera aleatória (3 a 5 segundos) nas requisições, para reduzir as chances de "rate limit"

    site = requests.get(url, headers=header)  # Utilizando requests para pegar a pagina passada no url
    # print(site) #testar se a resposta deu 200...REQUEST=OK

    link = BeautifulSoup(site.content, 'html.parser')  # Parser é um mecanismo de tradução/leitura do html para python
    # print(dados_pagina.prettify()) #Esse comando (do proprio beautifulsoup) deixa mais bonito o codigo HTML raspado

    tabela = link.find('tbody', class_='datatable-v2_body__8TXQk')  # aqui busca a PRIMEIRA <tag tbody> que possue a classe da tabela

    # Se a classe que contem a tabela for encontrada, extrai as linhas "tr"
    if tabela:
        rows = tabela.find_all('tr')

        # Itera sobre todas as linhas extraindo os dados
        for row in rows:
            cells = row.find_all('td')  # Pega todas as células de cada linha
            data = [cell.get_text(strip=True) for cell in cells]  # limpa o texto e coloca em uma lista
            print(data[1], data[-2]) #imprimir somente o "par de moeda" e sua varição em %
    time.sleep(espera)
