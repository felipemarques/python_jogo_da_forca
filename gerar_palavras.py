# Lista de palavras
palavras = [
    "python", "programacao", "desenvolvimento", "openai", "inteligencia",
    "computador", "algoritmo", "linguagem", "estrutura", "dados",
    "aprendizado", "maquina", "artificial", "interface", "usuario",
    "variavel", "funcao", "requisito", "analise", "projeto",
    "seguranca", "rede", "web", "servidor", "cliente",
    "frontend", "backend", "framework", "api", "docker",
    "git", "versionamento", "teste", "debug", "erro",
    "algoritmo", "estrutura", "condicional", "repeticao", "vetor",
    "matriz", "lista", "pilha", "fila", "ordenacao",
    "busca", "recursao", "heranca", "polimorfismo", "encapsulamento",
    "classe", "objeto", "metodo", "atributo", "construtor",
    "abstracao", "interface", "implementacao", "biblioteca", "pacote",
    "agil", "scrum", "kanban", "sprint", "produto",
    "cliente", "documentacao", "bug", "feature", "release",
    "hackathon", "code", "hack", "debug", "shell",
    "terminal", "console", "loop", "script", "compilacao",
    "interpretacao", "linguagem", "natural", "token", "compilador",
    "interpretador", "ambiente", "desenvolvimento", "producao", "teste",
    "producao", "modulo", "operador", "expressao", "declaracao"
]

# Caminho do arquivo
caminho_arquivo = "palavras.txt"

# Salvar a lista em um arquivo de texto
with open(caminho_arquivo, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(f"{palavra}\n")

print(f"A lista de palavras foi salva em '{caminho_arquivo}'.")
