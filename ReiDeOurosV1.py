from time import sleep


def encontrar_numero_mais_proximo(media, numeros):
    numero_mais_proximo = None
    diferenca_mais_proxima = float('inf')

    for numero in numeros:
        diferenca = abs(numero - media)
        if diferenca < diferenca_mais_proxima:
            diferenca_mais_proxima = diferenca
            numero_mais_proximo = numero

    return numero_mais_proximo


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
jogadores = []
pontos = 0
rodada = 1

for i in range(0, 5):
    jogadores.append(str(input(f'\033[4;91mK♦\033[m Nome do \033[91mJogador {i + 1}\033[m: ').capitalize().strip()))
    dados.append([jogadores[i], pontos])

mostrou_1 = False
mostrou_2 = False
mostrou_3 = False

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

        if dados[n][-1] >= -10:
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
    numero_encontrado = encontrar_numero_mais_proximo(resultado, numeros)

    print()
    print('Vamos ver o que cada jogador escolheu:')
    print()
    sleep(3)
    for i, k, j in dados:
        print(f'Mestre {i.ljust(10, ".")}\033[4;96m{j:>0}\033[m')
    sleep(2)
    print()
    print(f'A média de todos os números foi de {media}')
    print(f'O resultado de {media} multiplicado por 0.8 corresponde a {resultado:.1f}')

    n = 0
    sleep(4)
    for i, k, j in dados:
        if j == numero_encontrado and not len(dados) == 2:
            vencedor = i
            print(f'O Vencedor da rodada é \033[4;33mMestre {vencedor}\033[m')
        else:
            if len(dados) <= 4:
                dicionario = {}
                for item in dados:
                    nome, numero = item
                    if numero not in dicionario:
                        dicionario[numero] = []
                    dicionario[numero].append(nome)

                resultados = {numero: nomes for numero, nomes in dicionario.items() if len(nomes) > 1}

                if resultados:
                    for numero, nomes in resultados.items():
                        print(f'Numero {numero}: {" e ".join(nomes)}')

                else:
                    pass

            if len(dados) <= 3:
                dados[n][1] -= 2
                pontos = dados[n][1]
            else:
                dados[n][1] -= 1
                pontos = dados[n][1]

        if len(dados) == 2:
            if dados[0][-1] == 100 and dados[1][-1] == 100:
                dados[n][1] -= 2

            elif dados[0][-1] == 0 and dados[1][-1] == 0:
                dados[n][1] -= 2

            elif dados[0][-1] == 100 and dados[1][-1] == 0:
                print(f'O Vencedor da rodada é \033[4;33mMestre {dados[0][0]}\033[m')

            elif dados[0][-1] == 0 and dados[1][-1] == 100:
                print(f'O Vencedor da rodada é \033[4;33mMestre {dados[1][0]}\033[m')

            elif j == numero_encontrado:
                vencedor = i
                print(f'O Vencedor da rodada é \033[4;33mMestre {vencedor}\033[m')

            else:
                dados[n][1] -= 2
                pontos = dados[n][1]

        n += 1

    print()
    print('Houve mudança na pontuação entre os jogadores:')
    print()

    for i in range(0, len(dados)):
        del dados[i][-1]

    for i, k in dados:
        print(f'{i.ljust(15, ".")}[ \033[4;33m{k:>0}\033[m ]')

    num = 0
    for i, k in dados:
        if k <= -10:
            del dados[num]
            print(dados)
            num -= 1
            continue
        num += 1

    if len(dados) == 1:
        print(f'\033[4;91mK♦\033[m Jogo zerado! Parabéns Mestre {dados[0][0]} \033[4;91mK♦\033[m')

    rodada += 1
