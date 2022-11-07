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

def registeredClient():
    print('Olá Fulano, bem-vindo a WE-RJ Telecom!')

    userInputString = str(input('O que você precisa?\nCaso queira contratar ou trocar de plano escreva “Quero contratar” ou “Quero trocar de plano”:\n'))

    userInputString = userInputString.lower()

    if userInputString == True:
        if 'contratar' in userInputString:
            print('Ótimo! Temos os seguintes planos:\n200 Mbp/s\n400 Mbp/s\n500 Mbp/s\n1 Gbp/s\n')

            userOptionInput = str(input('Caso algum desses planos te interesse, escreva “Tenho interesse”, que você será redirecionado para um atendente.\nOu caso queira voltar para o menu anterior, digite “Voltar”.')).lower()

            if 'voltar' in userOptionInput:
                registeredClient()
            elif '200' in userOptionInput:
                pass
            else:
                print('Não entendi a sua mensagem, poderia digitar novamente?')
                ## chamar função novamente

