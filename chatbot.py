import time
import os

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def setPhoneNumber():
    ## Verificar telefones na lista de clientes
    pass

def firstMessage():
    print('Olá! Seja bem-vindo a WE-RJ Telecom!')

    userCpf = int(input('Nosso sistema identificou que este é o seu primeiro contato conosco, por favor, digite o seu CPF:'))
    userEmail = str(input('Digite Seu E-mail:'))
    userFirstName = str(input('Diga como você prefere ser chamado:'))

    newUser = {'cpf': userCpf, 'email': userEmail, 'firstName': userFirstName}

    return newUser

def newPlan(userChoice):

    loopWait = False

    clearConsole()
    print('Olá, recebi a sua escolha e vou te transferir para algum de nossos atendentes para que você siga com seu processo...\n')
    time.sleep(5)
    clearConsole()
    print('Aguardando atendente.')
    time.sleep(0.5)
    clearConsole()
    print('Aguardando atendente..')
    time.sleep(0.5)
    clearConsole()
    print('Aguardando atendente...')
    time.sleep(0.5)
    clearConsole()
    print('Aguardando atendente.')
    time.sleep(0.5)
    clearConsole()
    print('Aguardando atendente..')
    time.sleep(0.5)
    clearConsole()
    print('Aguardando atendente...')
    time.sleep(2)
    clearConsole()
    print('Infelizmente nenhum atendente está disponível no momento, iremos encerrar seu atendimento.')


def newPlanOption():
    print('Ótimo! Temos os seguintes planos:\n200 Mbp/s\n400 Mbp/s\n500 Mbp/s\n1 Gbp/s\n')

    userInternetSpeedOption = str(input('Caso algum desses planos te interesse, escreva “Tenho interesse”, que você será redirecionado para um atendente.\nOu caso queira voltar para o menu anterior, digite “Voltar”.\n')).lower()

    if 'voltar' in userInternetSpeedOption:
        registeredClient()
    elif '200' or '400' or '500' or '1' or '1 gb' or '1 gbps' or '1 gbp/s' or 'interesse' or 'quero' or 'interessado' in userInternetSpeedOption:
        newPlan(userInternetSpeedOption)
    else:
        print('Não entendi a sua mensagem, poderia digitar novamente?')
        newPlanOption()

def registeredClient():
    print('Olá Fulano, bem-vindo a WE-RJ Telecom!')

    userInputString = str(input('O que você precisa?\nCaso queira contratar ou trocar de plano escreva “Quero contratar” ou “Quero trocar de plano”:\n'))

    userInputString = userInputString.lower()

    if 'contratar' in userInputString:
        newPlanOption()

registeredClient()
