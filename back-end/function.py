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

def listar_produto():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY ID"
            )
            return cursor.fetchall()      
        except Exception as erro:
            print(f"Erro ao tew_pricebir Produtos: {erro}")
            return []
        finally:
            cursor.close()
            conexao.close()

def atualizar_produto(id, new_price, new_amount):
    conexao, cursor = conector() 
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s, quantidade = %s WHERE id = %s",
                (new_price, new_amount, id)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto atualizado com sucesso!")
            else:
                print("Nenhum produto encontrado com esse ID.")
        except Exception as erro:
            print(f"Erro ao tentar atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id,)
            )
            conexao.commit()
            if cursor.rowcount > 0:
                print("Produto removido do carrinho com sucesso!")
            else:
                print("Nenhum Produto foi encontrado em nosso almoxarifado.")
        except Exception as erro:
            print(f"Erro ao tentar inserir produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()
