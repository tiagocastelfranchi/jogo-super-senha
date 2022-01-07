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
print("As cores válidas são: AMARELO, VERDE, AZUL, ROXO, VERMELHO, LARANJA")
cores_senha = ['AMARELO', 'VERDE', 'AZUL', 'ROXO', 'VERMELHO', 'LARANJA']
senha = random.sample(cores_senha, 4)

# escolher o modo: ver senha ou não
# print(f'A senha gerada foi: {senha}')
print('Sua senha foi gerada! Boa sorte!')
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
