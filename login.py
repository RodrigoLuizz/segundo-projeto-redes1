from random import randint

class Pessoa:
    def __init__(self, nome, cpf, agencia, conta, senha):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.senha = senha

    def getnome(self):
        return self.nome

    def getcpf(self):
        return self.cpf

    def getagencia(self):
        return self.agencia

    def getconta(self):
        return self.conta

    def getsenha(self):
        """Retorna os digitos da senha"""
        digitos_key = [] 
        for digito in self.senha:
            digitos_key.append(int(digito))

        return digitos_key 



class Telalogin:
    
    def __init__(self, pessoa):
        self.lenght_key = 6 # Quantidade de digitos.
        self.digitos_usados = [] # Digitos usados para gerar os pares de digitos da senha
        self.list_digitos = {} # Pares de digitos usados na senha.
        self.pessoa = pessoa



    def _gerar_digito(self):
        '''Verifica se o digito já foi utilizado no sistema.'''
        digito = 0 
        while True:
            if digito not in self.digitos_usados:
                self.digitos_usados.append(digito)
                break
            else:
                digito = randint(1, 9)    
        return digito


    def _gerar_digitos(self):
        '''Gera os digitos que o usuário pode escolher.'''
        for indice in range(0,5):
            self.list_digitos[indice] = (self._gerar_digito(), self._gerar_digito())



    def _imprimir_tela(self):
        print("Escolha, na ordem correta, o índice onde se encontra o digito da sua senha: ")
        print()
        self._gerar_digitos()
        for key, value in self.list_digitos.items():
            print(f'{key} - {value[0]} ou {value[1]}')


    def _tela_login(self):
        self._imprimir_tela()
        indices_escolhidos = []
        for i in range(0, self.lenght_key):
             indice = int(input('Senha eletrônica: ')) # Lembrar que os índices começam em 1 e não em 0.
             while indice not in [0, 1, 2, 3, 4]:
                print("Indice invalido!")
                indice = int(input('Senha eletrônica: ')) 
             indices_escolhidos.append(indice)

        return indices_escolhidos


    def _validation(self):
        indices = self._tela_login()
        senha = self.pessoa.getsenha()
        login = True
        for index, valor in enumerate(indices):
            if senha[index] not in self.list_digitos[valor]:
                login = False
                break
        return login


    def mensagen_login(self):
        login_valid = self._validation()
        if login_valid:
            print(f'\nWELCOME TO APP SR. {self.pessoa.getnome()}')
        else:
            print('\nKEY INCORRECT')


        
        
    
pessoa = Pessoa('Rodrigo', '1290-', '16789', '1234', '103710')
login = Telalogin(pessoa)
login.mensagen_login()


