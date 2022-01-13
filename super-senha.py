import random

dicas = []
tentativa = 0

azul = []
amarelo = []
verde = []
roxo = []
vermelho = []
laranja = []

# randomização da senha
print("\nPara se tornar o mestre do Super Senha, você precisa acertar a ordem das cores geradas automaticamente.")
print("\nAs cores válidas são: AMARELO, VERDE, AZUL, ROXO, VERMELHO, LARANJA")
print("\nVocê consegue descobrir a ordem das 4 cores escolhidas?")
print("\n***ATENÇÃO***")
print(
    "\n- As cores não podem ser duplicadas \n- Você possuí 10 chutes para resolver o código\n- As respostas ao seu palpite serão [VAZIO] = a cor não está dentre as sorteadas, [PRETA] = a cor está correta, porém na posição errada e [BRANCA] = a cor está correta na posição correta")
print("- Aqui está um exemplo de como você deve realizar os chutes. 'Digite seu palpite separando as cores por vírgula: azul, vermelho, laranja, verde'.")
cores_senha = ['AMARELO', 'VERDE', 'AZUL', 'ROXO', 'VERMELHO', 'LARANJA']
senha = random.sample(cores_senha, 4)

# escolher o modo: ver senha ou não
print('\n*Sua senha foi gerada! Boa sorte!*')
print(f'\n~Senha gerada: {senha}')

flag = True
verdoufals = True

# tratamento do chute

while flag:
    chute = input(
        '\nDigite seu palpite separando as cores por vírgula: ').upper()
    chuteJoin = ''.join(chute)
    chuteSpace = chuteJoin.replace(' ', '')
    chuteSplit = chuteSpace.split(',')
    print(f'\nSeu chute foi {chuteSplit}!')

    if(len(chuteSplit) != 4):
        print('\nPor favor insira 4 cores válidas separadas por vírgula!')
        continue

    for cor in chuteSplit:
        if(cor != 'AMARELO' and cor != 'VERDE' and cor != 'AZUL' and cor != 'ROXO' and cor != 'VERMELHO' and cor != 'LARANJA'):
            print(
                '\nERRO: Valores inseridos inválidos. Digite apenas as cores permitidas.')
            verdoufals = False
            break
        else:
            verdoufals = True
            continue

    if (verdoufals == True):

        for i, item_cor in enumerate(chuteSplit):
            if(item_cor not in senha):
                dicas.append('VAZIO')
            elif(item_cor == senha[i]):
                dicas.append('BRANCA')
            else:
                dicas.append('PRETA')

        print(f'\nVocê possui {9- tentativa} tentativas! ')
        print(f'\nAs dicas geradas foram: {dicas}')

        for n, cor_pino in enumerate(chuteSplit):
            if(cor_pino == 'AZUL'):
                azul.append(0)
            if(cor_pino == 'AMARELO'):
                amarelo.append(0)
            if(cor_pino == 'VERDE'):
                verde.append(0)
            if(cor_pino == 'ROXO'):
                roxo.append(0)
            if(cor_pino == 'VERMELHO'):
                vermelho.append(0)
            if(cor_pino == 'LARANJA'):
                laranja.append(0)
        print(f'Você possui {10-len(azul)} pinos azuis.')
        print(f'Você possui {10-len(amarelo)} pinos amarelos.')
        print(f'Você possui {10-len(verde)} pinos verdes.')
        print(f'Você possui {10-len(roxo)} pinos roxos.')
        print(f'Você possui {10-len(vermelho)} pinos vermelhos.')
        print(f'Você possui {10-len(laranja)} pinos laranjas.')

        if (chuteSplit == senha):
            print(
                '\n---------------------------------------------------------------------')
            print(f'\nVOCÊ ACABA DE SE TORNAR O MESTRE DO SUPER SENHA! PARABÉNS!!!')
            flag = False
            break

        if (10-len(azul) <= 0):
            print('\nSeus pinos azuis acabaram. FIM DE JOGO!')
            flag = False

        if (10-len(amarelo) <= 0):
            print('\nSeus pinos amarelos acabaram. FIM DE JOGO!')
            flag = False

        if (10-len(verde) <= 0):
            print('\nSeus pinos verdes acabaram. FIM DE JOGO!')
            flag = False

        if (10-len(roxo) <= 0):
            print('\nSeus pinos roxos acabaram. FIM DE JOGO!')
            flag = False

        if (10-len(vermelho) <= 0):
            print('\nSeus pinos vermelhos acabaram. FIM DE JOGO!')
            flag = False

        if (10-len(laranja) <= 0):
            print('\nSeus pinos laranjas acabaram. FIM DE JOGO!')
            flag = False

        for i in dicas:
            tentativa += 1
            if tentativa < 10:
                dicas.pop()
                dicas.pop()
                dicas.pop()
                dicas.pop()
            else:
                print('Suas tentativas acabaram! FIM DE JOGO!')
                flag = False
                break
            print(
                '\n---------------------------------------------------------------------')

while True:
    denovo = input(
        "\nVocê gostaria de jogar novamente? [s/n]: ").lower()
    if denovo == 's':
        print(
            "\n------------------------------Novo Jogo------------------------------")
        break
    elif denovo == 'n':
        print(
            '\n---------------------------------------------------------------------')
        print("\n***Obrigado por jogar Super Senha! Até mais!***")
        print("\nJogo finalizado.\n")
        exit()
    else:
        print('\nInput inválido.')
        continue

print(
    '\n\n---------------------------------------------------------------------')
