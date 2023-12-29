import nltk
from nltk.corpus import words

# Baixar o corpus de palavras em português
nltk.download('words')

# Obter a lista de palavras em português
palavras_portuguesas = words.words()

# Filtrar para obter 10.000 palavras
palavras_10000 = palavras_portuguesas[:10000]

# Caminho do arquivo
caminho_arquivo = "palavras5.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras_10000:
        arquivo.write(f"{palavra}\n")

print(f"A lista de 10.000 palavras em português foi salva em '{caminho_arquivo}'.")
