#  Import

import random  #  escolher as palavras aleatorias 
from os import system, name  #  para verificar o sistema operacional 'cls' para windows, 'clear' para linux 

#  Função para limpar a tela a cada execução

def limpa_tela():
        
  #  windows    
  if name == 'nt':  #  'nt' é o nome dado para sistema windows nome interno do windows

      _ = system('cls')  #  _ é pra n retornar o que retorna não me interessa

  #  Mac ou Linux
  else:
    _ = system('clear')  

#  função do jogo

def game():
    
  limpa_tela()

  print("\nBem-vindo(a) ao jogo da forca!")
  print("Adivinhe a palavra abaixo:\n")

  #  lista de palavras para o jogo
  palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja'] 

  #  Escolhe randomicamente uma palavra
  palavra = random.choice(palavras)

  #  list comprehension
  letras_descobertas = ['_' for letra in palavra]

  #  número de chances
  chances = 6

  #  lista para as letras erradas
  letras_erradas = []

  #  Loop enquanto número de chances for maior do que zero
  while chances > 0:
  
    print("".join(letras_descobertas))  #  join faz uma junção do lado esquerdo e direito juntando o espaço com letras descobertas 
    print("\nchances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    #  tentativas
    tentativa = input("\nDigite uma letra: ").lower()  # lower letras minusculas

    #  condicional 
    if tentativa in palavra:
        index = 0
        for letra in palavra:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)
        
    #  condicional
    if "_" not in letras_descobertas:
      print("\nVocê venceu, a palavra era:", palavra)
      break

#  bloco main
if __name__ == "__main__":  #  indica que é um programa modulo python
  game()