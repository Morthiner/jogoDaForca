# import pandas as pd
# 
# # importar a base de dados
# paises_do_mundo = pd.read_excel('paises.xlsx')
# paises_do_mundo = paises_do_mundo[['Local', 'Continente']]
# 
# # visualizar a base de dados
# pd.set_option('display.max_columns', None)
# #print(paises_do_mundo)
# 
# # paises da europa
# paises_mask = paises_do_mundo['Continente'] == "Europa"
# tabela_paises_europa = paises_do_mundo[paises_mask]
# #print(tabela_paises_europa)
# 
# # tabela com apenas os paises
# paises_europa = tabela_paises_europa['Local']
# #print(paises_europa)
# 
# # transformando a coluna da tabela em um array com o nome dos paises da europa e formatando os nomes
# lista_paises = paises_europa.tolist()
# i = 0
# while i < len(lista_paises):
#     lista_paises[i] = unidecode.unidecode(lista_paises[i].lower())
#     i += 1
# print(lista_paises)

import random
import unidecode

paises = ['albania', 'alemanha', 'andorra', 'austria', 'belgica', 
'bielorrussia', 'bosnia e herzegovina', 'bulgaria', 'chipre', 
'croacia', 'dinamarca', 'eslovaquia', 'eslovenia', 'espanha', 'estonia', 'finlandia', 
'franca', 'georgia', 'grecia', 'hungria', 'irlanda', 'islandia', 'italia', 'kosovo', 'letonia', 
'liechtenstein', 'lituania', 'luxemburgo', 'macedonia do norte', 'malta', 'moldavia', 'monaco', 
'montenegro', 'noruega', 'paises baixos', 'polonia', 'portugal', 
'reino unido', 'republica tcheca', 'romenia', 'russia', 'san marino', 'servia', 'suecia', 'suica',
'ucrania', 'vaticano']

indice = len(paises) - 1
x = random.randint(0, indice)
pais = paises[x]
nome_oculto = "_" * len(pais)
temp = ""

print("-" * 50)
print("Jogo da forca \nAdivinhe o país europeu:")
print(nome_oculto)
round = 0

while round < 3:
    jogada = input("\ndigite uma letra: ")
    jogada = unidecode.unidecode(jogada.lower())
    if temp.replace("_", " ") == pais:
        print("Voce acertou! Fim de jogo")
        break
    elif jogada in pais:
        for letra in pais:
            if letra == jogada:
                lista_indexes = []
                # a funçao enumerate retorna para cada elemento da lista um array do tipo [index , caractere]
                for pos,char in enumerate(pais):
                    if(char == letra):
                        lista_indexes.append(pos)
                        for i in lista_indexes:
                            nome_oculto = nome_oculto[:i] + jogada + nome_oculto[i+1:]
                            temp = nome_oculto
        print("\n",temp,"\n")
    else:
        round += 1
        print("Você tem mais {} tentativas".format(3 - round))
print("-" * 50)
