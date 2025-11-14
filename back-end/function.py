from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
                )
            """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()


def cadastrar_produto(name_produto, category_produto, price_produto, amount_produto):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (name_produto, category_produto, price_produto, amount_produto)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar cadastrar o Produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
