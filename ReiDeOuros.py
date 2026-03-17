from time import sleep
from random import randint, choice


def encontrar_numero_mais_proximo(media, numeros):
    numero_mais_proximo = None
    diferenca_mais_proxima = float('inf')

    for numero in numeros:
        diferenca = abs(numero - media)
        if diferenca < diferenca_mais_proxima:
            diferenca_mais_proxima = diferenca
            numero_mais_proximo = numero

    return numero_mais_proximo


def jogador_virtual(jogadores_restantes):
    
    if jogadores_restantes == 2:
        estrategia = choice([
            lambda: 0,
            lambda: 100,
            lambda: randint(1, 20)
        ])
    else:
        estrategia = choice([
            lambda: randint(0, 100),
            lambda: randint(35, 45),
            lambda: randint(20, 30),
            lambda: randint(10, 20)
        ])

    return estrategia()


print('Jogo: ')
sleep(1)
print('\033[93mConsurso de beleza\033[m.')
sleep(2)
print('Dificuldade: Rei de \033[91mOuros\033[m')
sleep(3)
print()

print('''Cada jogador presente (5) deverá escolher um número de 0 a 100. Para cada número escolhido
será feito uma média sobre cada número e depois multiplicado por 0,8. O jogador que escolher o número
mais próximo do resultado ganha a rodada. 
Os restantes perderão 1 ponto dos 10 que são concebidos. Se um jogador chegar a 0, será adicionado uma regra nova.

\033[92mBoa sorte.\033[m''')

dados = []
pontos = 0
rodada = 1

num_humanos = int(input("Quantos jogadores humanos? "))

for i in range(num_humanos):
    nome = input(f'Nome do Jogador {i+1}: ').capitalize().strip()
    dados.append([nome, 0, False])

nomes = [
    "Lucas", "Ana", "Bruno", "Marina", "Carlos",
    "Julia", "Pedro", "Camila", "Rafael", "Larissa",
    "Mateus", "Beatriz", "Thiago", "Isabela", "Gustavo"
]
while len(dados) < 5:
    nome = choice(nomes)
    dados.append([nome, 0, True])
    for i, j in enumerate(nomes):
        if nome == j:
            del nomes[i]

mostrou_1 = mostrou_2 = mostrou_3 = False

while True:
    numeros = []
    n = 0
    print()
    print(f'Rodada {rodada}... Comecem.')
    sleep(2)

    while True:

        if len(dados) <= 4 and not mostrou_1:
            mostrou_1 = True
            print()
            print('Uma nova regra será acrescentada:')
            print('''\033[4;91mK♦\033[m Se duas ou mais pessoas escolherem o mesmo número, o número escolhido se tornará inválido,
o que significa que elas perderão dois pontos cada. \033[4;91mK♦\033[m''')
            print()

        if len(dados) <= 3 and not mostrou_2:
            mostrou_2 = True
            print()
            print('Uma nova regra será acrescentada:')
            print('''\033[4;91mK♦\033[m Se houver uma pessoa que escolha o número exato, 
a penalidade do perdedor será dobrada. \033[4;91mK♦\033[m''')
            print()

        if len(dados) == 2 and not mostrou_3:
            mostrou_3 = True
            print()
            print('Uma nova regra será acrescentada:')
            print('\033[4;91mK♦\033[m Se alguém escolher 0, o jogador que escolher 100 é o vencedor. \033[4;91mK♦\033[m')
            print()

        if dados[n][1] > -10:

            if dados[n][2]:  # BOT
                num_jog = jogador_virtual(len(dados))
                print(f'Mestre \033[4;97m{dados[n][0]}\033[m informe seu número: {num_jog}')
            else:
                num_jog = int(input(f'Mestre \033[4;97m{dados[n][0]}\033[m informe seu número: '))

            if num_jog > 100 or num_jog < 0:
                print()
                print('\033[4;91mK♦\033[m \033[4;93mApenas é válido um número de 0 a 100.\033[m \033[4;91mK♦\033[m')
                continue
            else:
                numeros.append(num_jog)

            n += 1

            if len(numeros) == len(dados):
                break

        else:
            continue

    for i in range(0, len(dados)):
        dados[i].append(numeros[i])

    media = sum(numeros) / len(numeros)
    resultado = media * 0.8

    if len(dados) > 2:
        numero_encontrado = encontrar_numero_mais_proximo(resultado, numeros)

    if len(dados) == 2:
        a = dados[0][-1]
        b = dados[1][-1]

        if a == 0 and b == 100:
            vencedor = dados[1][0]

        elif b == 0 and a == 100:
            vencedor = dados[0][0]

        else:
            vencedor = dados[0][0] if abs(a - resultado) < abs(b - resultado) else dados[1][0]

        print(f'O Vencedor da rodada é \033[4;33mMestre {vencedor}\033[m')

    print()
    print('Vamos ver o que cada jogador escolheu:')
    print()
    sleep(3)

    for jogador in dados:
        nome = jogador[0]
        numero = jogador[-1]
        print(f'Mestre {nome.ljust(10, ".")}\033[4;96m{numero:>0}\033[m')

    sleep(2)

    print()
    print(f'A média de todos os números foi de {media}')
    print(f'O resultado de {media} multiplicado por 0.8 corresponde a {resultado:.1f}')

    n = 0
    sleep(4)

    for jogador in dados:
        i = jogador[0]
        k = jogador[1]
        j = jogador[-1]
   
        if len(dados) != 2 and j == numero_encontrado:
            vencedor = i
            print(f'O Vencedor da rodada é \033[4;33mMestre {vencedor}\033[m')

        else:

            if len(dados) == 2:
                if dados[n][0] != vencedor:
                    dados[n][1] -= 1

            elif len(dados) <= 3:
                dados[n][1] -= 2
                pontos = dados[n][1]
            else:
                dados[n][1] -= 1
                pontos = dados[n][1]

        n += 1

    print()
    print('Houve mudança na pontuação entre os jogadores:')
    print()

    for i in range(0, len(dados)):
        del dados[i][-1]

    for jogador in dados:
        print(f'{jogador[0].ljust(15, ".")}[ \033[4;33m{jogador[1]:>0}\033[m ]')

    dados = [jogador for jogador in dados if jogador[1] > -10]
    rodada += 1

if len(dados) == 1:
    print(f'\033[4;91mK♦\033[m Jogo zerado! Parabéns Mestre {dados[0][0]} \033[4;91mK♦\033[m')
