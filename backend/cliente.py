#!/usr/bin/env python3
#coding: 'utf-8'

import socket as sc
from random import randint
import json 

class Telalogin:
    
    def __init__(self):
        self.lenght_key = 6 # Quantidade de digitos.
        self.digitos_usados = [] # Digitos usados para gerar os pares de digitos da senha
        self.list_digitos = {} # Pares de digitos usados na senha.


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


    def tela_login(self):
        self._imprimir_tela()
        indices_escolhidos = []
        for i in range(0, self.lenght_key):
             indice = int(input('Senha eletrônica: ')) # Lembrar que os índices começam em 1 e não em 0.
             while indice not in [0, 1, 2, 3, 4]:
                print("Indice invalido!")
                indice = int(input('Senha eletrônica: ')) 
             indices_escolhidos.append(str(indice))
        return indices_escolhidos



class Cliente:
    '''Clinte que se conectara com o servidor.'''
    
    def __init__(self, HOST, PORT):
        self.host = HOST # IP do Servidor que deseja se conectar.. 
        self.port = PORT # Porta usada para conectar-se ao servidor.
        self.login = Telalogin()
        self.indices = self.login.tela_login()
        self.list_digitos = self.login.list_digitos


    def _conncetion(self):
        """Estabelecer a conexão com o Servidor."""
        client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        client.connect((self.host, self.port))
        return client 


    def enviar_information(self):
        """Envia informações necessárias para efetuar o login."""
        cliente = self._conncetion()
        data = json.dumps({"info_1": self.indices, "info_2":self.list_digitos})
        cliente.send(data.encode())
        # Recebendo a informação
        data = cliente.recv(1000000)
        print(data.decode())

clinte = Cliente('127.0.0.1', 4040)
clinte.enviar_information()
