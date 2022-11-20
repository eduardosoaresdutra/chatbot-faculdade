import time
import os

def clearConsole():
    os.system('cls' if os.name=='nt' else 'clear')

def checkPhoneNumber():
    phoneNumbersFile = open('phoneNumbers.txt', 'r')

    userPhoneNumber = str(input('Por favor, digite seu telefone: '))
    userPhoneNumber = userPhoneNumber + '\n'

    for line in phoneNumbersFile:
        if line.rstrip('\n') == userPhoneNumber.rstrip('\n'):
            phoneNumbersFile.close()
            registeredClient()
        else:
            phoneNumbersFile.close()
            firstMessage()

def firstMessage():
    print('Olá! Seja bem-vindo a WE-RJ Telecom!')

    userCpf = int(input('Nosso sistema identificou que este é o seu primeiro contato conosco, por favor, digite o seu CPF:'))
    userEmail = str(input('Digite Seu E-mail:'))
    userPhoneNumber = str(input('Digite seu telefone:'))
    userFirstName = str(input('Diga como você prefere ser chamado:'))

    newUser = {'cpf': userCpf, 'email': userEmail, 'phoneNumber': userPhoneNumber, 'firstName': userFirstName}

    clients = open('clients.txt', 'w')
    clients.write(str(newUser))
    clients.write('\n')
    clients.close()

    userPhoneNumber = userPhoneNumber + '\n'

    phoneNumbersFile = open('phoneNumbers.txt', 'w')
    phoneNumbersFile.write(userPhoneNumber)
    phoneNumbersFile.close()

    registeredClient()

def callAttendant(userChoice):

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
    
    return False


def newPlanOption():
    print('Ótimo! Temos os seguintes planos:\n200 Mbp/s\n400 Mbp/s\n500 Mbp/s\n1 Gbp/s\n')

    userInternetSpeedOption = str(input('Caso algum desses planos te interesse, escreva “Tenho interesse”, que você será redirecionado para um atendente.\nOu caso queira voltar para o menu anterior, digite “Voltar”.\n')).lower()

    if 'voltar' in userInternetSpeedOption:
        registeredClient()
    elif '200' or '400' or '500' or '1' or '1 gb' or '1 gbps' or '1 gbp/s' or 'interesse' or 'quero' or 'interessado' in userInternetSpeedOption:
        callAttendant(userInternetSpeedOption)
    else:
        print('Não entendi a sua mensagem, poderia digitar novamente?\n')
        newPlanOption()

def supportOption():
    userInput = str(input('Certo, tente retirar o modem da tomada, aguardar cerca de 20 segundos, e ligue novamente em seguida. Após isso, verifique se a sua conexão retornou ao normal.\n\nSe retornou, digite “Sim”, caso ainda estiver com problemas, digite “Não":')).lower()

    if userInput == 'sim':
        print('Ótimo, agradecemos seu contato!')
        return False
    elif userInput == 'não':
        callAttendant(userInput)
    else:
        print('Não foi possível entender a sua mensagem, por favor tente novamente.\n')
        supportOption()

def billingOption():
    print('Sua última fatura foi enviada para o e-mail do cadastro!\nObrigado pelo contato, seu atendimento será encerrado...\n')
    return False

def registeredClient():
    print('Olá, bem-vindo a WE-RJ Telecom!')

    userInputString = str(input('O que você precisa?\nCaso queira contratar ou trocar de plano escreva “Quero contratar” ou “Quero trocar de plano”.\nCaso esteja com problemas de conexão, escreva "suporte".\nCaso queira seu boleto, digite "boleto":\n'))

    userInputString = userInputString.lower()

    if 'contratar' or 'trocar plano' or 'aumentar velocidade' or 'mudar plano' or 'velocidade' or 'plano' in userInputString:
        newPlanOption()
    elif 'suporte' or 'lenta' or 'internet lenta' or 'internet esta lenta' or 'problema' or 'velocidade' in userInputString:
        supportOption()
    elif 'boleto' or 'segunda via' or '2ª via' or 'fatura' in userInputString:
        billingOption()
    else:
        print('Não foi posível entender a sua mensagem, seu atendimento será encerrado.')
        return False

while(True):
    checkPhoneNumber()
