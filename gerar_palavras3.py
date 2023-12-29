# Lista de palavras em português
palavras = [
    "abacaxi", "banana", "cachorro", "dado", "elefante",
    "foca", "girafa", "hipopotamo", "iguana", "jacare",
    "kiwi", "leão", "macaco", "navio", "ocelote",
    "pato", "quati", "rato", "sapo", "tigre",
    "uva", "vaca", "wolverine", "xaxim", "yeti",
    "zebra", "abobora", "bacalhau", "cacau", "dromedario",
    "escorpiao", "flamingo", "gazela", "hibisco", "icaro",
    "jaguar", "kiwi", "lambari", "maracuja", "nabo",
    "ocelote", "pacoca", "quindim", "rabanada", "sururu",
    "tamarindo", "urso", "vindima", "waffle", "xerife",
    "yeti", "zebu", "abracadabra", "bambu", "cacamba",
    "dengue", "eletronico", "fubá", "geleia", "hamburguer",
    "iluminado", "jabuticaba", "karaoke", "limonada", "magenta",
    "nanquim", "oculos", "pacote", "quadro", "rabanete",
    "safira", "teclado", "ultravioleta", "vitamina", "xadrez",
    "yoga", "zodíaco", "alfinete", "biblioteca", "camundongo",
    "diamante", "estrela", "foguete", "guitarra", "helicóptero",
    "instinto", "jubileu", "karate", "luminaria", "mamute",
    "ninja", "oculto", "paralelepipedo", "quimera", "radiante",
    "sincero", "taciturno", "unico", "vigoroso", "waffle",
    "xilogravura", "yakult", "zumbi"
]

# Caminho do arquivo
caminho_arquivo = "palavras3.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(f"{palavra}\n")

print(f"A lista de palavras em português foi salva em '{caminho_arquivo}'.")
