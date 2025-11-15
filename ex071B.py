from time import sleep
from datetime import date
from datetime import datetime
from random import randint

#Banco de dados de e-mails
banco_de_dados = [
    {
        'id': 56435454,
        'nome completo': 'Guilherme Santos',
        'idade': 28,
        'data de nasc': '24/03/1996',
        'endereço': 'Rua Albino Salvador',
        'número': '3014',
        'cpf': '48932156488',
        'celular': '11999999999',
        'e-mail': 'guilherme@gmail.com',
        'senha': '123',
        'conta': '95625700',
        'saldo': 372.24,
        'extrato': [
            {
                'id': 35413542,
                'valor': -645.54,
                'data': '25/06/2024',
                'descrição': 'Pix enviado'
            },
            {
                'id': 56465445,
                'valor': -26.50,
                'data': '29/06/2024',
                'descrição': 'Compra no crédito'
            },
            {
                'id': 35143543,
                'valor': 200.00,
                'data': '02/07/2024',
                'descrição': 'Pix recebido'
            },
            {
                'id': 52453451,
                'valor': -89.37,
                'data': '02/07/2024',
                'descrição': 'Compra no crédito'
            }
        ],
        'chave_pix_aleatória': 356333353678564453,
        'limite_cartão': 700
    },
    {
        'id': 98468463,
        'nome completo': 'Roberta Farias dos Santos',
        'idade': 49,
        'data de nasc': '02/04/1975',
        'endereço': 'Avenida Rodolfo de Almeida',
        'número': '36',
        'cpf': '12368437844',
        'celular': '11988888888',
        'e-mail': 'roberta@gmail.com',
        'senha': 'FariasR10',
        'conta': '32678100',
        'saldo': 14.91,
        'extrato': [],
        'chave_pix_aleatória': 719245651757357124,
        'limite_cartão': 250
    },
    {
        'id': 35435748,
        'nome completo': 'Jorge Oliveira da Silva Souza',
        'idade': 35,
        'data de nasc': '02/01/1989',
        'endereço': 'Estrada Farias do Sul',
        'número': '963',
        'cpf': '24512356556',
        'celular': '13977777777',
        'e-mail': 'jorge@hotmail.com',
        'senha': 'jOrjao09@',
        'conta': '71336500',
        'saldo': 1320.64,
        'extrato': [],
        'chave_pix_aleatória': 157839970852388136,
        'limite_cartão': 2100
    },
    {
        'id': 45689734,
        'nome completo': 'Mateus Ribeiro Rodrigues',
        'idade': 35,
        'data de nasc': '29/11/1989',
        'endereço': 'Rua Novo Horizonte',
        'número': '47',
        'cpf': '24545230511',
        'celular': '11966666666',
        'e-mail': 'mateus@gmail.com',
        'senha': '22RRmateuz',
        'conta': '98745200',
        'saldo': 8.90,
        'extrato': [],
        'chave_pix_aleatória': 231551725968588017,
        'limite_cartão': 'null'
    }
]

ano_atual = date.today().year
hoje = datetime.now().strftime('%d/%m/%Y')
num = []
info_login = ''
email = ''

# Painél indeex
print('=' * 30)
print(f'\033[1:7:34m{'BANCO GS':^30}\033[m')
print('=' * 30)
print('\033[1mOlá, seja bem-vindo ao Banco GS!\033[m')
def login():
    print('\n\033[4mFaça o seu login para iniciarmos a sua sessão\033[m\n')
    infos = ['EMAIL', 'E-MAIL', 'CPF', 'CELULAR', 'CONTA']
    for each in range(1, len(infos)):
        print(infos[each])
    info_login = str(input('Qual informação você quer usar?\n')).strip().upper()
    #Cabeçalho do LOGIN
    if info_login in infos:
        print('\n\033[1:7:36m LOGIN \033[m')
    else:
        while True:
            info_login = str(input('Digite uma das opções abaixo:\n'
                                   '[E-MAIL / CPF / CELULAR / CONTA] ')).strip().upper()
            if info_login in 'EMAIL''E-MAIL''CPF''CELULAR''CONTA':
                print('\n\033[1:7:36m LOGIN \033[m')
                break
    return
login()
def inputEmail():
    return str(input('Endereço de E-mail: ')).strip().lower()
def inputCpf():
    return str(input('CPF: ')).strip().lower()
def inputCelular():
    return str(input('Digite seu Celular sem Pontuações: ')).strip()
def inputConta():
    return str(input('Conta: ')).strip()
def open_account():
    cadastrar = str(input('\nE-mail não identificado!\n'
                             'Faça o seu cadastro em nosso sistema para abrir uma conta.\n'
                    'Digite [SIM] para continuar ou [NÃO] para encerrar \n')).strip().upper()[0]
    if cadastrar in '1S':
        cadastroSIM(email)
    elif cadastrar in '2N':
        cadastroNAO()
    else:
        cadastroERRO()
def cadastroSIM(mail):
    print(f'Endereço de E-mail: {mail}')
    nome_sign = str(input('Nome Completo: ')).strip().capitalize()
    nasc_sign = str(input('Data de Nascimento: '))
    nasc = int(nasc_sign[-4:])
    idade_sign = ano_atual - nasc
    endereco_sign = str(input('Endereço: '))
    numero_sign = str(input('Número: '))
    cpf_sign = str(input('CPF: ')).strip()
    celular_sign = str(input('Celular: '))
    senha_sign = str(input('Senha: ')).strip()
    new_password = senha_sign
    confirm_senha = str(input('Confirme Sua Senha: ')).strip()
    if confirm_senha != new_password:
        print('Confirmação de senha inválida! Tente Novamente')
        senha_sign = str(input('Senha: ')).strip()
        new_password = senha_sign
        confirm_senha = str(input('Confirme Sua Senha: ')).strip()
        if confirm_senha != new_password:
            print('\033[1:31mDesculpe, a senha digitada não corresponde a mesma informação anteriormente!\033[m\n'
                  'Tente novamente!')
    for c in range(0, 6):
        n = randint(1, 9)
        num.append(n)
    num.append(0)
    num.append(0)
    print(num)
    new_user = {
        'nome completo': nome_sign,
        'idade': idade_sign,
        'data de nasc': nasc_sign,
        'endereço': endereco_sign,
        'número': numero_sign,
        'cpf': cpf_sign,
        'celular': celular_sign,
        'e-mail': mail,
        'senha': senha_sign,
        'conta': num
    }
    banco_de_dados.append(new_user.copy())
    print('Aguarde um momento, estamos trabalhando para abrir a sua conta...')
    sleep(3)
    print('Parabéns, você foi aprovado em nosso sistema!')
    sleep(1)
    print('Por favor, faça o login para acessar a sua conta!\n')
    print('\033[1:7:36m LOGIN \033[m')
    email = inputEmail()
    if checker_dados(banco_de_dados, 'e-mail', email):
        senha(email, 'e-mail')
    else:
        print('Senha inválida!')
    return
def cadastroNAO():
    print('Ok! Estaremos a disposição caso você deseje se juntar a nós!!!\n'
          '\033[4mAté logo\033[m')
def cadastroERRO():
    resp = ''
    for open in range(1, 4):
        openacc_inva = str(input('Desculpa, não conseguimos te entender.\n'
                                 'Digite novamente a sua resposta com "SIM" ou "NÃO"\n')).strip().upper()[0]
        if openacc_inva in 'S':
            cadastroSIM(email)
            resp = 'S'
            break
        elif openacc_inva in 'N':
            cadastroNAO()
            resp = 'N'
            break
    if resp == '':
        print('Não foi possível obter a informação!\n'
              'Pedimos desculpa pelo incoveniente ocorrido. Pedimos que reinicie o sistema e tente novamente. Obrigado!')

password = []
def senha(dado, indice):
    senha = str(input('Senha: ')).strip()
    if checker_senha(banco_de_dados, dado, indice, senha):
        print(f'\n\033[1mSeja bem vindo, {get_info(banco_de_dados, dado, indice, 'nome completo')}!\033[m\n')
        password.append('ok')
    else:
        print('Senha inválida!')
        return
def get_info(lista, infoOut, indice, infoIn):
    for dicionario in lista:
        if dicionario.get(indice) == infoOut:
            return dicionario.get(infoIn)
    return None
def checker_senha(lista, nome, indice, valor):
    for dicionario in lista:
        if dicionario.get(f'{indice}') == nome:
            return valor in dicionario.values()
    return False
def checker_dados(lista, indice, valor):
    for dicionario in lista:
        if dicionario.get(indice) == valor:
            return valor in dicionario.values()
    return False
def menu():
    print('=-' * 30)
    print('1) SALDO\n'
          '2) PIX\n'
          '3) CARTÕES\n'
          '4) SAQUE\n'
          '5) \033[4mSAIR\033[m')
    resp = int(input('DIGITE UMA OPÇÃO: \n'))
    if resp == 1:
        saldo()
    elif resp == 2:
        pix()
    elif resp == 3:
        cartoes()
    elif resp == 4:
        saque()
    elif resp == 5:
        login()
def saldo():
    print('=-' * 30)
    print(f'O seu saldo é de R${get_info(banco_de_dados, email, 'e-mail', 'saldo'):.2f}')
    sleep(0.5)
    resp = int(input('\n1) EXTRATO\n'
                      '2) MENU\n'))
    if resp == 1:
        extrato()
    elif resp == 2:
        sleep(0.5)
        menu()
    else:
        print('Desculpa, não te entendi! Digite uma das opções acima\n'
              'Vamos tentar novamente... Aguarde')
        sleep(1.5)
        saldo()
def extrato():
    print('=-' * 27)
    print(f'Saldo: R${get_info(banco_de_dados, email, 'e-mail', 'saldo'):.2f}', end='')
    print('\n\033[1mEXTRATO\033[m')
    print('=-' * 27)
    for chave in get_info(banco_de_dados, email, 'e-mail', 'extrato'):
        # print(chave)
            print(f'{chave['valor']:<10}', end='')
            print(f'{chave['descrição']:^30}', end='')
            print(f'{chave['data']:>13}')
            print('-' * 53)
    resp = str(input('1) VOLTAR AO MENU \n'))
    if resp == '1':
        menu()
    elif resp == '':
        menu()
    else:
        print('Opção inválida! Tente novamente.')
        sleep(1.5)
        extrato()
def pix():
    print('=-' * 27)
    print('1) PAGAR\n'
          '2) RECEBER\n'
          '3) MENU')
    resp = int(input('Digite sua opção: \n'))
    if resp == 1:
        pixPagar()
    elif resp == 2:
        pixReceber()
    elif resp == 3:
        menu()
    else:
        print('Opção inválida! Tente novamente.')
        sleep(1.5)
        pix()
def pixPagar():
    chaves = str(input('Para quem você quer pagar?\n'
                       '\033[37m(Chave, Pix copia e cola, QR Code ou Favorito)\033[m\n')).strip().lower()
    if chaves == 'menu':
        menu()
    elif chaves == 'voltar':
        pix()
    elif chaves == 'chave':
        print('\n1) CPF\n'
              '2) CELULAR\n'
              '3) E-MAIL')
        chave = str(input('\033[1mDigite uma opção para a chave pix:\033[m\n')).strip().lower()
        if chave == 'menu':
            menu()
        if chave == 'voltar':
            pixPagar()
        if chave == '1': #Registro pela chave cpf
            chave_pix('cpf')
        elif chave == '2': #Registro pela chave celular
            chave_pix('celular')
        elif chave == '3': #Registro pela chave e-mail
            chave_pix('e-mail')
        else:
            print('Opção inválida! Tente novamente.')
            sleep(1.5)
            pixPagar()
    elif chaves == 'pix copia e cola': #pix copia e cola
        chave_pix('chave_pix_aleatória')
    elif chaves == 'qr code''qrcode':
        print('\033[7:33mFunção indisponível no momento! Por favor, tente mais tarde.\033[m\n')
        sleep(1)
        pix()
    elif chaves == 'favorito':
        print('\033[7:33mFunção indisponível no momento! Por favor, tente mais tarde.\033[m\n')
        sleep(1)
        pix()
    elif chaves == '':
        pixPagar()
    else:
        print('Opção inválida! Tente novamente.')
        sleep(1.5)
        pixPagar()
def pixReceber():
    chave_aleatoria = randint(100000000000000000, 999999999999999999)
    personalizado = str(input('Personalizar chave pix? \n')).strip().upper()
    if personalizado in 'SIM''':
        valor = int(input('R$ '))
        print(f'\n\033[1:7:33m{'REVISÃO':^30}\033[m')
        print('-' * 30)
        print(f'\033[1mR$ {valor}\033[m\n'
              f'\033[37mValor a receber\033[m')
        print('-' * 30)
        print(f'\n\033[1mChave Aleatória:\033[m\n'
              f'\033[37m{chave_aleatoria}\033[m')
        editar = str(input('\033[37m(Caso deseje editar a chave, digite "1") \033[m'))
        if editar == '1':
            print('\n\033[1mAlterar chave\033[m')
            print('1) Chave de Celular\n'
                  f'\033[37m{get_info(banco_de_dados, email, 'e-mail', 'celular')}\033[m\n')
            print('2) Chave de E-mail\n'
                  f'\033[37m{get_info(banco_de_dados, email, 'e-mail', 'e-mail')}\033[m')
            resp = int(input())
            if resp == 1:
                confirm = str(input('\033[1mConfirmar alteração de chave? \033[m')).strip().upper()
                if confirm in 'SIM''':
                    chave_aleatoria = get_info(banco_de_dados, email, 'e-mail', 'celular')
                    print('-' * 30)
                    print(f'\033[1mR$ {valor}\033[m\n'
                          f'\033[37mValor a receber\033[m')
                    print('-' * 30)
                    print(f'\nChave de Celular:\n'
                          f'{chave_aleatoria}')
                elif confirm in 'NÃO''NAO':
                    pass
                else:
                    invalido = str(input('Não entendi! Caso, realmente deseje alterar a sua chave pix, digite "voltar" e tente novamente!\n')).strip().lower()
                    if invalido == 'voltar':
                        pixReceber()
                    else:
                        pix()
            elif resp == 2:
                confirm = str(input('\033[1mConfirmar alteração de chave? \033[m')).strip().upper()
                if confirm in 'SIM''':
                    chave_aleatoria = get_info(banco_de_dados, email, 'e-mail', 'e-mail')
                    print('-' * 30)
                    print(f'\033[1mR$ {valor}\033[m\n'
                          f'\033[37mValor a receber\033[m')
                    print('-' * 30)
                    print(f'\nChave de E-mail:\n'
                          f'{chave_aleatoria}')
                elif confirm in 'NÃO''NAO':
                    pass
                else:
                    invalido = str(input(
                        'Não entendi! Caso, realmente deseje alterar a sua chave pix, digite "voltar" e tente novamente!\n')).strip().lower()
                    if invalido == 'voltar':
                        pixReceber()
                    else:
                        pix()
            else:
                invalido = str(input(
                    'Não entendi! Caso, realmente deseje alterar a sua chave pix, digite "voltar" e tente novamente!\n')).strip().lower()
                if invalido == 'voltar':
                    pixReceber()
                else:
                    pix()
        description = str(input('Adicionar Mensagem: \033[37m(Opcional) \033[m')).strip()
        confirm = str(input('\033[1mGerar chave? \033[m')).strip().upper()
        if confirm in 'SIM''':
            print()
            print('=-' * 27)
            print('✅\n'
                  f'\033[1mChave pix gerada com sucesso!\033[m\n'
                  f'\033[37m{chave_aleatoria}\033[m\n'
                  f'R$ {valor}')
            if description != '':
                print(f'Descrição: \033[4m{description}\033[m')
            print()
            menu()
        elif confirm in 'NÃO''NAO':
            pix()
        else:
            print('Desculpa, não te entendi!\n'
                  'Tentar novamente... Aguarde')
            sleep(1.5)
            pixPagar()
    elif personalizado in 'NÃO''NAO':
        description = str(input('Adicionar Mensagem: \033[37m(Opcional) \033[m')).strip()
        confirm = str(input('\033[1mGerar chave? \033[m')).strip().upper()
        if confirm in 'SIM''':
            print()
            print('=-' * 27)
            print('✅\n'
                  f'\033[1mChave pix gerada com sucesso!\033[m\n'
                  f'\033[37m{chave_aleatoria}\033[m')
            if description != '':
                print(f'Descrição: \033[4m{description}\033[m')
            print()
            menu()
        elif confirm in 'NÃO''NAO':
            pix()
        else:
            print('Desculpa, não te entendi!\n'
                  'Tentar novamente... Aguarde')
            sleep(1.5)
            pixPagar()
    else:
        pix()
def cartoes():
    print('-' * 30)
    print(f'\033[1:7:35m{'CARTÕES':^30}\033[m')
    print('-' * 30)
    print(f'\033[1:7:37m{'Limite de Crédito':^30}\033[m\n')
    transacoes_encontradas.clear()
    transacoes_cartao(banco_de_dados)
    limite_utilizado = 0
    for valor in transacoes_encontradas:
        limite_utilizado += valor
    limite_disponivel = get_info(banco_de_dados, email, 'e-mail', 'limite_cartão')
    limite_disponivel -= limite_utilizado
    print(f'\033[1m{'Limite total':^30}\033[m')
    print(f'\033[1m{get_info(banco_de_dados, email, 'e-mail', 'limite_cartão'):^30}\033[m')
    print('\033[37mUtilizado\033[m', end='')
    print(f'\033[37m{'Disponível':>20}\033[m')
    print(f'{limite_utilizado}', end='')
    print(f'{limite_disponivel:>21}\n')
    resp = str(input('1) VOLTAR AO MENU \n'))
    if resp == '1':
        menu()
    elif resp == '':
        menu()
    else:
        print('Opção inválida! Tente novamente.')
        sleep(1.5)
        cartoes()

transacoes_encontradas = []
def transacoes_cartao(lista):
    for dicionario in lista:
        for transacao in dicionario['extrato']:
            if condicao(transacao):
                transacoes_encontradas.append(transacao['valor'])
    return transacoes_encontradas
def condicao(transacao):
    return transacao['descrição'] == 'Compra no crédito'

def getMes(data_str):
    data = datetime.strptime(data_str, '%d/%m/%Y')
    meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro',
        10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    return meses[data.month]
def update(lista, indice, infoIn, indiceID, infoOut):
    id = get_info(banco_de_dados, infoIn, f'{indiceID}', 'id')
    novo_valor = infoOut
    for dicionario in lista:
        if dicionario['id'] == id:
            if indice in dicionario:
                dicionario[indice] = novo_valor
                return
            else:
                print(f'Ocorreu um erro! Por favor, tente mais tarde.')
                return False
    print(f"Registro com ID {id} não encontrado.")
def updateExtrato(lista, indice, infoIn, indiceID, infoOut):
    id = get_info(banco_de_dados, infoIn, f'{indiceID}', 'id')
    novo_valor = infoOut
    for dicionario in lista:
        if dicionario['id'] == id:
            if indice in dicionario:
                dicionario[f'{indice}'].append(novo_valor)
                return
            else:
                print(f'Ocorreu um erro! Por favor, tente mais tarde.')
                return
    # print(f"Registro com ID {id} não encontrado.")
def chave_pix(indice):
    choice = str(input('\nChave Pix: ')).strip()
    if choice.isdigit():
        choice = int(choice)
    contaReceive = get_info(banco_de_dados, choice, indice, 'conta')
    contaCode = []
    contaCode.append(contaReceive)
    nomeRept = get_info(banco_de_dados, choice, indice, 'nome completo')
    if checker_dados(banco_de_dados, indice, choice):
        print('=-' * 27)
        print(f'Saldo em conta: R${get_info(banco_de_dados, email, 'e-mail', 'saldo')}\n')
        print('Pagar para:\n'
              f'\033[1m{nomeRept}\033[m\n')
        valor = int(input('R$ '))
        print()
        print('=-' * 15)
        print(f'\033[1:7:33m{'REVISÃO':^30}\033[m')
        print('-' * 30)
        print(f'\033[1mR$ {valor}\033[m\n'
              f'{nomeRept}')
        print('-' * 30)
        print('\033[1mPagar quando:\n'
              '🗓️ Agora\033[m\n'
              f'\033[1:37m{hoje}\033[m')
        print('\n\033[1mQuem vai receber:\033[m\n'
              f'\033[37mNome: \033[m\033[1m{nomeRept}\033[m\n'
              f'\033[37mConta: \033[m\033[1m{contaCode[0][0:3]}****0\033[m\n'
              '\033[37mInstituição: \033[m\033[1mBanco GS (Brasil) S.A.\033[m\n'
              f'\033[37mChave de {indice.capitalize()}: \033[m\033[1m{choice}\033[m\n')
        description = str(input('Adicionar Mensagem: \033[37m(Opcional) \033[m')).strip()
        confirm = str(input('\033[1mConfirmar transação? \033[m')).strip().upper()[0]
        if confirm == 'S':
            saldoAtual = get_info(banco_de_dados, email, 'e-mail', 'saldo')
            if valor <= saldoAtual:
                print()
                print('=-' * 27)
                print('✅\n'
                      f'\033[1mPix enviado!\033[m\n'
                      f'R$ {valor}')
                if description != '':
                    print(f'Descrição: \033[4m{description}\033[m')
                print()
                pix = valor
                saldoNovo = saldoAtual - pix
                update(banco_de_dados, 'saldo', email, 'e-mail', saldoNovo)
                # update no extrato!
                num_id = []
                for volta in range(0, 8):
                    id_num = randint(1, 9)
                    num_id.append(id_num)
                extratoNovo = {
                    'id': num_id,
                    'valor': f'-{valor}',
                    'data': hoje,
                    'descrição': 'Pix enviado'
                }
                updateExtrato(banco_de_dados, 'extrato', email, 'e-mail', extratoNovo)
                # conta_do_receptor
                saldoAtual2 = get_info(banco_de_dados, choice, indice, 'saldo')
                saldoNovo2 = saldoAtual2 + pix
                update(banco_de_dados, 'saldo', choice, indice, saldoNovo2)
                # update no extrato(RECEPTOR)!
                num_id = []
                num_id.clear()
                for volta in range(0, 8):
                    id_num = randint(1, 9)
                    num_id.append(id_num)
                extratoNovo2 = {
                    'id': num_id,
                    'valor': f'{valor}',
                    'data': hoje,
                    'descrição': 'Pix recebido'
                }
                updateExtrato(banco_de_dados, 'extrato', choice, indice, extratoNovo2)
                # print(get_info(banco_de_dados, choice, f'{indice}', 'extrato'))
                menu()
            else:
                print('\033[31mNão foi possível concluir a operação!\n'
                      'Saldo insuficiente\033[m\n')
                pixPagar()
        elif confirm == 'N':
            print('\033[31mTransação cancelada!\033[m\n')
            pixPagar()
        else:
            print('Desculpa, não te entendi!\n'
                  'Tentar novamente... Aguarde')
            sleep(1.5)
            pixPagar()
    else:
        print('\033[31mChave pix não encontrada!\033[m\n')
        pixPagar()
#Sistema de saque!
#Contagem de quantas cédulas serão utilzadas no saque!
def saque():
    fifty = twenty = ten = one = 0

    sacar = float(input('Que valor você quer sacar? R$'))
    saldo = sacar

    while True:
        if saldo - 50 >= 0:
            saldo -= 50
            fifty += 1
        if saldo - 50 < 0:
            break
    while True:
        if saldo - 20 >= 0:
            saldo -= 20
            twenty += 1
        if saldo - 20 < 0:
            break
    while True:
        if saldo - 10 >= 0:
            saldo -= 10
            ten += 1
        if saldo - 10 < 0:
            break
    while True:
        if saldo - 1 >= 0:
            saldo -= 1
            one += 1
        if saldo - 1 < 0:
            break

    print(saldo)
    print(f'\nTotal de {fifty} cédulas de R$50\n'
          f'Total de {twenty} cédulas de R$20\n'
          f'Total de {ten} cédulas de R$10\n'
          f'Total de {one} cédulas de R$1')

#login e senha!
if info_login in 'EMAIL''E-MAIL':
    email = inputEmail()
    if checker_dados(banco_de_dados,'e-mail', email):
        senha(email, 'e-mail')
    else:
        open_account()
elif info_login in 'CPF':
    cpf = inputCpf()
    if checker_dados(banco_de_dados, 'cpf', cpf):
        senha(cpf, 'cpf')
    else:
        open_account()
elif info_login in 'CELULAR':
    celular = inputCelular()
    if checker_dados(banco_de_dados, 'celular', celular):
        senha(celular, 'celular')
    else:
        open_account()
elif info_login in 'CONTA':
    conta = inputConta()
    if checker_dados(banco_de_dados, 'conta', conta):
        senha(conta, 'conta')
    else:
        open_account()
if 'ok' in password:
    menu()



