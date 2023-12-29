import nltk
from nltk.corpus import floresta, machado
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Baixar os corpora Floresta e Machado de Assis em português
nltk.download('floresta')
nltk.download('machado')
nltk.download('omw')  # Open Multilingual Wordnet

# Obter as listas de palavras dos corpora Floresta e Machado de Assis
palavras_floresta = floresta.words()
palavras_machado = machado.words()

# Combinar as duas listas
palavras_portuguesas = palavras_floresta + palavras_machado

# Filtrar palavras com mais de 3 caracteres e que sejam alfabéticas
palavras_filtradas = [palavra.lower() for palavra in palavras_portuguesas if palavra.isalpha() and len(palavra) > 3 and not palavra.endswith("s")]

# Remover palavras duplicadas
palavras_filtradas = list(set(palavras_filtradas))

# Lematização
lemmatizer = WordNetLemmatizer()
palavras_lematizadas = [lemmatizer.lemmatize(palavra) for palavra in palavras_filtradas]

# Função para obter sinônimos de uma palavra usando WordNet
def obter_sinonimos_wordnet(palavra):
    sinonimos = set()
    for synset in wordnet.synsets(palavra, lang='por'):
        for lemma in synset.lemmas('por'):
            sinonimos.add(lemma.name().lower())
    return list(sinonimos)

# Dividir as palavras por letra inicial
palavras_por_letra = {}
for palavra in palavras_lematizadas:
    letra_inicial = palavra[0]
    if letra_inicial not in palavras_por_letra:
        palavras_por_letra[letra_inicial] = []
    palavras_por_letra[letra_inicial].append(palavra)

# Gerar 10 palavras por letra inicial (ou menos, se não houver)
palavras_geradas = set()  # Convertendo para um conjunto para evitar repetições
for letra, palavras_letra in palavras_por_letra.items():
    for palavra in palavras_letra[:500]:
        sinonimos = obter_sinonimos_wordnet(palavra)
        palavras_geradas.add(palavra)
        palavras_geradas.update(sinonimos)

# Caminho do arquivo
caminho_arquivo = "palavras8.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras_geradas:
        arquivo.write(f"{palavra}\n")

print(f"A lista de palavras em português foi salva em '{caminho_arquivo}'.")
