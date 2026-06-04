import sqlite3

# Conectar o banco de dados (ou criar, se não existir)

def conectarBanco() :
    conexao = sqlite3.connect('meu_banco.db')
    return conexao

# Criaremos uma tabela nesse banco de dados

def criarTabela() :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )              
    ''')
    conexao.commit()
    conexao.close()
    
# Inserindo dado na tabela
    
def inserirUsuarios(nome, idade) :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?, ?)             
    ''', (nome, idade))
    conexao.commit()
    conexao.close()
    
# Listar as informações    
    
def listarUsuarios() :
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
    
criarTabela()
inserirUsuarios('Caio', 39)
inserirUsuarios('Guilherme', 25)
inserirUsuarios('Leandro', 39)
inserirUsuarios('Carlos', 58)
inserirUsuarios('Daniel', 30)
inserirUsuarios('Vinicius', 22)

listarUsuarios()