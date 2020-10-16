#!/usr/bin/env python3
# -*- coding: utf-8 -*

from flask import Flask, request, abort
#import os
import base64
import re
#app_path = os.path.dirname(os.path.realpath(__file__))
app_path = '/scripts/python/' 
app = Flask('desafio')

@app.route('/funcionarios/criar', methods=['POST'])
def criar():
        if request.method == 'POST':
            nome = request.args['nome']
            login = request.args['login']
            password = request.args['pw']
            decoded_password = base64.b64decode(password).decode('utf-8')
            validacao_password(decoded_password)
            arquivo_add(nome, login, decoded_password)
            return "Funcionário adicionado com sucesso! Nome: {}, Login: {}".format(nome, login), 201
            
@app.route('/funcionarios/apagar/<login>', methods=['DELETE'])
def apagar(login):
        if request.method == 'DELETE':
            #login = request.args['login']
            arquivo_del(login)
            return "Funcionário {} removido com sucesso!".format(login), 200
            
def arquivo_add(nome, login, senha):
    f = open(app_path + "/data.txt", "a+")
    validacao_login(f, login)
    f.write('ADD "{}", "{}", "{}"\n'.format(nome, login, senha))
    f.close()
    
def arquivo_del(login):
    f = open(app_path + "/data.txt", "a+")
    validacao_login(f, login)
    f.write('DISABLE "{}"\n'.format(login))
    f.close()
    
def validacao_login(f, login):
    f.seek(0)
    linha = f.readline();
    while linha:
        primeira_palavra = linha.split()[0]
        dados = re.findall(r'\"(.+?)\"', linha)
        if (primeira_palavra == "ADD"):
            if (login == dados[1]):
                abort(400, 'Usuario ja existente no arquivo de hoje.')
        elif (primeira_palavra == "DISABLE"):
            if (login == dados[0]):
                abort(400, 'Usuario ja existente no arquivo de hoje.')
        linha = f.readline();
        
def validacao_password(password):
    if (len(password) < 10):
        abort(400, 'A senha precisa ter pelo menos 10 caracteres.')
    elif (re.search('[0-9]',password) is None):
        abort(400, 'A senha precisa ter pelo menos um numero.')
    elif (re.search('[A-Z]',password) is None):
        abort(400, 'A senha precisa ter pelo menos uma letra maiuscula.')
    elif (re.search('[a-z]',password) is None):
        abort(400, 'A senha precisa ter pelo menos uma letra minuscula.')
  
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8080')
