# Imports 
from datetime import date
import sqlite3

# Banco de dados
database = sqlite3.connect('database_usuarios.db')
cursor = database.cursor()

# Cria tabela
#cursor.execute("CREATE TABLE usuarios (n_conta integer, nome_do_usuario text, senha integer, extrato integer, debito integer)")
cursor.execute("INSERT INTO usuarios VALUES(200, 'Usuário de teste02', 12345678, 0, 0)")
database.commit()

# Printa dados
cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

#-------------------------------------------------------------------------------

# Classe Principal
class usuario():
    def __init__(self, I_numero_conta, I_nome_usuario, I_senha):
        self.n_conta = I_numero_conta
        self.nome_usuario = I_nome_usuario
        self.__senha = I_senha
        self.extrato = 0
        self.debito = 0

    def deposito(self, valor):
        usuario.extrato += valor

    def saque(self, valor):
        if usuario.extrato >= valor:
            usuario.extrato -= valor
            return "Saque concluido"

        else:
            return "Você não tem saldo para fazer este saque"

    def empretimo(self, valor, tempo):
        pass

        
    
