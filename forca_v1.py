# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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
class Hangman():

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        if self.letter in self.word:
            return True
        else:
            return False
        
    # Método para verificar se o jogo terminou
    def hangman_over(self, tentativas):
        self.tentativas = tentativas
        chances = 6
        if tentativas == chances:
            return True
        else:
            return False        
        
    # Método para verificar se o jogador venceu
    def hangman_won(self, letras_corretas):
        self.lista = letras_corretas
        letras_pendentes = [x for x in self.word if x not in self.lista]
        if len(letras_pendentes)==0:
            return True
        
    # Método para não mostrar a letra no board
    def hide_word(self, word, letras_corretas):
        if len(letras_corretas) == 0:
            for i in list(word):
                print("_", end=' ')
        else:
            for i in range(len(list(word))):
                if word[i] in letras_corretas:
                    print(word[i], end=' ')
                else:
                    print("_", end=' ')            

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self, tentativas, letras_corretas, letras_erradas):
        print(board[tentativas])
        print('\nPalavra: ', end =' ')
        self.hide_word(self.word, letras_corretas)
        print("\n\nLetras erradas: \n")
        for let in range(len(letras_erradas)):
            if len(letras_erradas) == 0:
                print("\n")
            else:
                print(letras_erradas[let])
        print("\nLetras corretas: \n")
        for let in range(len(letras_corretas)):
            if len(letras_corretas) == 0:
                print("\n")
            else:
                print(letras_corretas[let])
        
# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

# Função Main - Execução do Programa
def main():

    # Objeto
    
    game = Hangman(rand_word())
    tentativas = 0
    letras_erradas = []
    letras_corretas = []
    over = False
    
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    
    while not over:
        game.print_game_status(tentativas, letras_corretas, letras_erradas)
        letter = input('\nDigite uma letra: ')
        if letter not in letras_erradas and letter not in letras_corretas:
            tentativa = game.guess(letter)
        else:
            print('Opa! Você já tentou esta letra. Tente outra!')
            continue
        if not tentativa:
            letras_erradas.append(letter)
            tentativas += 1
        else:
            letras_corretas.append(letter)
            tentativas + 0
        if game.hangman_won(letras_corretas):
            break
        else:
            over = game.hangman_over(tentativas)
    

    # Verifica o status do jogo
    
    game.print_game_status(tentativas, letras_corretas, letras_erradas)    

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won(letras_corretas):
        print ('\nParabéns! Você venceu!!')
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.word)
        
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa        
if __name__ == "__main__":
    main()
