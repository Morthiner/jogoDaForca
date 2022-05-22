import random

estagios = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fim_do_jogo = False
lista_paises = ['albania', 'alemanha', 'andorra', 'austria', 'belgica', 
'bielorrussia', 'bosnia e herzegovina', 'bulgaria', 'chipre', 
'croacia', 'dinamarca', 'eslovaquia', 'eslovenia', 'espanha', 'estonia', 'finlandia', 
'franca', 'georgia', 'grecia', 'hungria', 'irlanda', 'islandia', 'italia', 'kosovo', 'letonia', 
'liechtenstein', 'lituania', 'luxemburgo', 'macedonia do norte', 'malta', 'moldavia', 'monaco', 
'montenegro', 'noruega', 'paises baixos', 'polonia', 'portugal', 
'reino unido', 'republica tcheca', 'romenia', 'russia', 'san marino', 'servia', 'suecia', 'suica',
'ucrania', 'vaticano']
palavra_escolhida = random.choice(lista_paises)
tamanho_palavra = len(palavra_escolhida)

vidas = 6
print(f'A solução é {palavra_escolhida}.')

display = []
for _ in range(tamanho_palavra):
    display += "_"

while not fim_do_jogo:
    palpite = input("Escolha uma letra: ").lower()

    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            display[posicao] = letra
    if palpite not in palavra_escolhida:
        vidas -= 1

    print(f"{' '.join(display)}")

    print(estagios[vidas])
    if vidas == 0:
        fim_do_jogo = True
        print("Você perdeu.")
    if "_" not in display:
        fim_do_jogo = True
        print("Você ganhou.")