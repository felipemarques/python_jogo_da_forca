import requests
from bs4 import BeautifulSoup

# Função para obter palavras de uma página da web
def obter_palavras_online():
    url = "https://www.palavrasque.com/palavras-mais-bonitas/"
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    palavras = [palavra.text.lower() for palavra in soup.find_all('span', {'class': 'ql-editor'})]
    return palavras

# Obtém palavras online
palavras = obter_palavras_online()

# Caminho do arquivo
caminho_arquivo = "palavras4.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(f"{palavra}\n")

print(f"A lista de 10.000 palavras foi salva em '{caminho_arquivo}'.")
