import sqlite3

# Conectando ao banco de dados

conn = sqlite3.connect("exemplo.db")

cursor = conn.cursor()

# ID do produto a ser excluído

produto_id = 2  # Suponha que queiramos excluir o produto com ID 2

# Comando SQL para excluir o produto

excluir_produto = "DELETE FROM Produtos WHERE id = ?"

# Executando o comando SQL de exclusão

cursor.execute(excluir_produto, (produto_id,))

# Confirmando as alterações

conn.commit()

# Fechando a conexão

conn.close()
