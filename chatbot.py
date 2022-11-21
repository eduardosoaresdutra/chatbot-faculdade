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
    
    exit()


def newPlanOption():
    print('Ótimo! Temos os seguintes planos:\n200 Mbp/s\n400 Mbp/s\n500 Mbp/s\n1 Gbp/s\n')

    userInternetSpeedOption = str(input('Caso algum desses planos te interesse, escreva “Tenho interesse”, que você será redirecionado para um atendente.\nOu caso queira voltar para o menu anterior, digite “Voltar”.\n')).lower()

    if 'voltar' in userInternetSpeedOption:
        registeredClient()
    elif userInternetSpeedOption in ('200', '400', '500', '1', '1 gb', '1 gbps', '1 gbp/s', 'interesse', 'quero', 'interessado'):
        callAttendant(userInternetSpeedOption)
    else:
        print('Não entendi a sua mensagem, poderia digitar novamente?\n')
        newPlanOption()

def supportOption():
    userInput = str(input('Certo, tente retirar o modem da tomada, aguardar cerca de 20 segundos, e ligue novamente em seguida. Após isso, verifique se a sua conexão retornou ao normal.\n\nSe retornou, digite “Sim”, caso ainda estiver com problemas, digite “Não":')).lower()

    if userInput == 'sim':
        print('Ótimo, agradecemos seu contato!')
        exit()
    elif userInput == 'não':
        callAttendant(userInput)
    else:
        print('Não foi possível entender a sua mensagem, por favor tente novamente.\n')
        supportOption()

def billingOption():
    print('Sua última fatura foi enviada para o e-mail do cadastro!\nObrigado pelo contato, seu atendimento será encerrado...\n')
    exit()

def registeredClient():
    checkVar = False

    if checkVar == False:
        print('Olá, bem-vindo a WE-RJ Telecom!')
        checkVar = True

    userInputString = str(input('O que você precisa?\nCaso queira contratar ou trocar de plano escreva “Quero contratar” ou “Quero trocar de plano”.\nCaso esteja com problemas de conexão, escreva "suporte".\nCaso queira seu boleto, digite "boleto":\n'))

    userInputString = userInputString.lower()

    if userInputString in ('contratar', 'trocar plano', 'aumentar velocidade', 'mudar plano', 'mudar o plano', 'mudar de plano', 'trocar plano', 'trocar de plano', 'trocar o plano', 'velocidade', 'plano'):
        newPlanOption()
    elif userInputString in ( 'suporte', 'lenta', 'internet lenta', 'internet esta lenta', 'problema', 'velocidade'):
        supportOption()
    elif userInputString in ('boleto', 'segunda via', '2ª via', 'fatura'):
        billingOption()
    else:
        print('Não foi posível entender a sua mensagem...')
        registeredClient() 
        

while(True):
    checkPhoneNumber()
