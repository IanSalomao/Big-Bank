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


        
    
