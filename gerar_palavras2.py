from faker import Faker

# Criar uma instância do Faker com idioma em português
# faker = Faker('pt_BR')
faker = Faker()

# Gerar 10.000 palavras aleatórias
palavras = [faker.word() for _ in range(10000)]

# Caminho do arquivo
caminho_arquivo = "palavras2.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(f"{palavra}\n")

print(f"A lista de 10.000 palavras foi salva em '{caminho_arquivo}'.")
