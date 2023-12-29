import nltk
from nltk.corpus import floresta, machado

# Baixar os corpora Floresta e Machado de Assis em português
nltk.download('floresta')
nltk.download('machado')

# Obter as listas de palavras dos corpora Floresta e Machado de Assis
palavras_floresta = floresta.words()
palavras_machado = machado.words()

# Combinar as duas listas
palavras_portuguesas = palavras_floresta + palavras_machado

# Filtrar palavras com mais de 3 caracteres e que sejam alfabéticas
palavras_filtradas = [palavra.lower() for palavra in palavras_portuguesas if palavra.isalpha() and len(palavra) > 3]

# Remover palavras duplicadas
palavras_filtradas = list(set(palavras_filtradas))

# Dividir as palavras por letra inicial
palavras_por_letra = {}
for palavra in palavras_filtradas:
    letra_inicial = palavra[0]
    if letra_inicial not in palavras_por_letra:
        palavras_por_letra[letra_inicial] = []
    palavras_por_letra[letra_inicial].append(palavra)

# Gerar 10 palavras por letra inicial (ou menos, se não houver)
palavras_geradas = []
for letra, palavras_letra in palavras_por_letra.items():
    palavras_geradas.extend(palavras_letra[:1000])

# Caminho do arquivo
caminho_arquivo = "palavras7.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras_geradas:
        arquivo.write(f"{palavra}\n")

print(f"A lista de palavras em português foi salva em '{caminho_arquivo}'.")
