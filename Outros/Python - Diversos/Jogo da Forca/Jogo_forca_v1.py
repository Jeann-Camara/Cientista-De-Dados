#------------------------------------- Jogo da Forca ---------------------------------------

import random

# Tabuleiro
board = ['''

>>>>>>>>>>boneco_forca<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Boneco_forca:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.missed_letters = []
        self.guessed_letters = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.palavra and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.palavra and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def boneco_forca_fim(self):
        return self.boneco_forca_venceu() or (len(self.missed_letters) == 6)

    # Método para verificar se o jogador venceu
    def boneco_forca_venceu(self):
        if '_' not in self.hide_palavra():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ''
        for letter in self.palavra:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters:
            print(letter, )
        print()
        print('Letras corretas: ', )
        for letter in self.guessed_letters:
            print(letter, )
        print()


# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Método Main - Execução do Programa
def main():
    # Objeto
    game = Boneco_forca(rand_palavra())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.boneco_forca_fim():
        game.print_game_status()
        user_input = input('\n Digite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.boneco_forca_venceu():
        print('\n Você venceu!')
    else:
        print('\n Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\n Fim de jogo!\n')


# Executa o programa
if __name__ == "__main__":
    main()
