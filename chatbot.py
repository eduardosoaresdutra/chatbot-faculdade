def firstMessage():
    print('Olá! Seja bem-vindo a WE-RJ Telecom!')

    userCpf = int(input('Nosso sistema identificou que este é o seu primeiro contato conosco, por favor, digite o seu CPF:'))
    userEmail = str(input('Digite Seu E-mail:'))
    userFirstName = str(input('Diga como você prefere ser chamado:'))

    newUser = {'cpf': userCpf, 'email': userEmail, 'firstName': userFirstName}

    return newUser

firstMessage()