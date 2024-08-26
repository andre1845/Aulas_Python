import mysql.connector

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='nome_do_banco_de_dados'
)

cursor = conexao.cursor()

# Exemplo de execução de um comando SQL
cursor.execute('SELECT * FROM usuarios')

# Obter resultados
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Fechar a conexão
conexao.close()
