#!/usr/bin/env python3
#coding:'utf-8'

from multiprocessing import connection
import socket as sc
import json
from sqlite3 import connect


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


class Server:
    
    '''Servidor de checagem de senha.'''

    def __init__(self, PORT, pessoa): # Inicializador da classe. 
        self.port = PORT # Porta de conexão do servidor.
        self.pessoa = pessoa
        self.indices = []
        self.list_digitos = {}
        self.connection = self._run_server()[0] # Pego apenas a conexão para deixar salva


    def _run_server(self):
        """Subir o servidor."""
        server = sc.socket(sc.AF_INET, sc.SOCK_STREAM) # Criando o objeto Socket
        server.bind(('', self.port)) # Abrindo a conexão localmente
        server.listen(2) # Numero de conexoes
        print('CONECTADO!')
        connection, addres = server.accept()
        return connection, addres


    def _recive_data_cliente(self):
        """Recebe os dados vindo do cliente"""
        data = self.connection.recv(1024) # Receber o nome do arquivo desejado. 
        data = json.loads(data.decode())
        self.indices = data.get("info_1")
        self.list_digitos = data.get("info_2")


    def _validation(self):
        """Verifica se o usuário digitou a senha corretaemente."""
        self._recive_data_cliente()
        senha = self.pessoa.getsenha()
        login = True
        for index, valor in enumerate(self.indices):
            if senha[index] not in self.list_digitos[valor]:
                login = False
                break
        return login


    def mensagen_login(self):
        login_valid = self._validation()
        if login_valid:
            self.connection.send(f'\nWELCOME TO APP SR. {self.pessoa.getnome()}'.encode())
        else:
            self.connection.send('\nKEY INCORRECT'.encode())
        self.connection.close()


pessoa = Pessoa('Rodrigo', '1290', '16789', '1234', '103710')
server = Server(4040, pessoa)
server.mensagen_login()
