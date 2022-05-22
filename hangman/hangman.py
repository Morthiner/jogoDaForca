import random
from hangman_art import estagios, logo
from hangman_words import lista_paises

fim_do_jogo = False
palavra_escolhida = random.choice(lista_paises)
tamanho_palavra = len(palavra_escolhida)
vidas = 6

print(logo)
print(f'A solução é {palavra_escolhida}.')

display = []
for _ in range(tamanho_palavra):
    display += "_"

while not fim_do_jogo:
    chute = input("Escolha uma letra: ").lower()
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