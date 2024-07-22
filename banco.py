import sqlite3

# Função para inicializar o banco de dados (cria as tabelas se não existirem)
def inicializar_banco():
    conn = sqlite3.connect('cookies.db')
    c = conn.cursor()

    # Cria a tabela pedidos
    c.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cookie TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL,
            cliente TEXT NOT NULL,
            whatsapp TEXT NOT NULL  -- Adicionado o campo whatsapp
        )
    ''')

    # Cria a tabela feedbacks
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Função para adicionar pedido de cookie ao banco de dados
def add_pedido(cookie, quantidade, preco, cliente, whatsapp):  # Ajustado para incluir whatsapp
    conn = sqlite3.connect('cookies.db')
    c = conn.cursor()
    c.execute('INSERT INTO pedidos (cookie, quantidade, preco, cliente, whatsapp) VALUES (?, ?, ?, ?, ?)', (cookie, quantidade, preco, cliente, whatsapp))
    conn.commit()
    conn.close()
    
# Função para adicionar feedback ao banco de dados
def add_feedback(nome, feedback):
    conn = sqlite3.connect('cookies.db')
    c = conn.cursor()
    c.execute('INSERT INTO feedbacks (nome, feedback) VALUES (?, ?)', (nome, feedback))
    conn.commit()
    conn.close()

# Função para atualizar um pedido no banco de dados
def update_pedido(pedido_id, cookie, quantidade, preco, cliente):
    conn = sqlite3.connect('cookies.db')
    c = conn.cursor()
    c.execute('''
        UPDATE pedidos 
        SET cookie = ?, quantidade = ?, preco = ?, cliente = ?
        WHERE id = ?
    ''', (cookie, quantidade, preco, cliente, pedido_id))
    conn.commit()
    conn.close()

# Inicializa o banco de dados quando este script for executado diretamente
if __name__ == "__main__":
    inicializar_banco()
