import os
import time
import random


def clear_screen():
    clear = lambda: os.system('clear')
    clear()


def selecionar_palavra():
    arquivo = open('palavras7.txt', 'r')
    palavras = arquivo.readlines()
    arquivo.close()
    palavra: str = random.choice(palavras).strip()
    return palavra


def exibir_forca(tentativas):
    forca = [
        """
         ------
         |    |
         |
         |
         |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |    |
         |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
         -
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
         -
        """
    ]

    # Verificar se tentativas está dentro dos limites da lista
    if tentativas < len(forca):
        return forca[tentativas]
    else:
        return forca[-1]


def exibir_palavra(palavra: str, ):
    global letrasCorretas, letrasErradas
    return ''.join(letra if letra in letrasCorretas else '_' for letra in palavra)


def exibir_barrinha_energia(energia, energiaMax=10):
    barra = "❤" * energia
    espacos = " " * (energiaMax - energia)
    print(f"Energia: [{barra}{espacos}]")


def verificarEnergia(energia, palavra):
    if energia == 0:
        print(exibir_forca(-1))
        print(f'Palavra correta: {palavra}', 'mas ...')
        raise Exception(f'Sua energia acabou, fim de jogo.')


maxNames = 0
letrasDigitadas = []
letrasErradas = set()
letrasCorretas = set()
tentativas = 0
novoJogo = True
palavra = ''
energia = 5
energiaMaxima = 5

try:

    while True:
        print(f' ======= Jogo da Forca ======= ')
        print('Author: Felipe Marques <contato@felipemarques.com.br>')

        if novoJogo:
            palavra = selecionar_palavra()

        exibir_barrinha_energia(energia, energiaMaxima)
        verificarEnergia(energia, palavra)
        print(exibir_forca(len(letrasErradas)))

        palavra_oculta = exibir_palavra(palavra)

        # verificar se o jogador ganhou.
        if palavra == palavra_oculta:
            print('🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆')
            print('🏆🏆🏆🏆🏆 Você ganhou! 🏆🏆🏆🏆🏆🏆🏆')
            print('🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆')
            exit(0)

        # print('Palavra: ', palavra)
        print('Palavra oculta: ', palavra_oculta, '(', len(palavra_oculta), ') caracteres')
        # print('Letras digitadas: ')
        # print(letrasDigitadas)
        # print('Letras corretas: ')
        # print(letrasCorretas)
        print('Letras erradas: ', len(letrasErradas))
        print(letrasErradas)

        letra = input('Digite uma letra: ')

        if letra in palavra:
            letrasCorretas.add(letra)
        else:
            energia -= 1
            letrasErradas.add(letra)

        letrasDigitadas.append(letra)

        maxNames = maxNames + 1
        tentativas += 1
        novoJogo = False

        clear_screen()

except Exception as e:
    print(e)
