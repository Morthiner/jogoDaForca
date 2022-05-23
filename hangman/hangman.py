from replit import clear
import random
from hangman_art import estagios, logo
from hangman_words import paises_europa, paises_mundo, paises_asia

modo_jogo = 0
modalidade = []

while modo_jogo < 1 or modo_jogo > 3:
    clear()
    modo_jogo = int(input(" Modalidades:\n\n 1 - Países do mundo\n 2 - Países da europa\n 3 - Países da ásia\n\n> "))
    print("-"*50)
    if modo_jogo == 1:
        modalidade = paises_mundo
    elif modo_jogo == 2:
        modalidade = paises_europa
    elif modo_jogo == 3:
        modalidade = paises_asia
    else:
        print("\nModalidade inválida. Tente novamente.\n")

clear()

fim_do_jogo = False
palavra_escolhida = random.choice(modalidade)
tamanho_palavra = len(palavra_escolhida)
vidas = 6

print(logo)
print(f'A solução é {palavra_escolhida}.')

display = []
for _ in range(tamanho_palavra):
    display += "_"

while not fim_do_jogo:
    chute = input("Escolha uma letra: ").lower()
    
    clear()

    if chute in display:
      print("Você já chutou essa letra")

    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == chute:
            display[posicao] = letra

    if chute not in palavra_escolhida:
        print(f"Você chutou {chute}, esta letra não pertence a palavra. Você perdeu uma vida.")
        vidas -= 1

    print(f"{' '.join(display)}")

    print(estagios[vidas])
    if vidas == 0:
        fim_do_jogo = True
        print("Você perdeu.")
    if "_" not in display:
        fim_do_jogo = True
        print("Você ganhou.")