import pyodbc # or any other database library you are using
from typing import Type
from vendedor import Vendedor  # Ensure this import matches your project structure
from produto import Produto  # Ensure this import matches your project structure
    # Ensure you have the necessary database library installed  
class Banco_de_Dados:
    def __init__(self,db_driver = "{SQL SERVER}",db_server ="GPSPNB001632\SQLEXPRESS", db_database="Python", user='sa', password='sql@2023'): # Replace with your connection details
        self.db_driver = db_driver
        self.db_server = db_server  
        self.db_database = db_database
        self.user = user
        self.password = password
        # Add connection initialization here if needed

    def _connect(self):
        try:
            # Replace with your database connection code
            conn = pyodbc.connect(f'DRIVER={self.db_driver};SERVER={self.db_server};DATABASE={self.db_database};UID={self.user};PWD={self.password};')
            conn.autocommit = True  # Set autocommit to True if you want to avoid manual commits 
            # For SQLite, you might use:
            print("Database connection established.")
            return conn
        except pyodbc.Error as ex:
            print("Error connecting to database:", ex)
        return None

    def _close(self, conn):
        """Closes the database connection."""
        if conn:
            print("Closing database connection.")
            conn.close()


    def selecionar_produto(self):
        """Selects all products from the produto table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL SELECT statement
                cursor.execute("SELECT * FROM produto")
                produtos = cursor.fetchall()
                obj_produtos = []
                for produtos in produtos:
                    obj_produto = Produto(produtos[1], produtos[3], produtos[2], produtos[0], produtos[4])  # Adjust indices based on your table structure
                    obj_produtos.append(obj_produto)
                return obj_produtos
            
            except Exception as e:
                print(f"Error selecting produtos: {e}")
            finally:
                self._close(conn)

    def inserir_produto(self, produto: Type[Produto]):
        """Inserts a new product into the produto table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL INSERT statement
                cursor.execute("INSERT INTO produto (nome, preco, empresa, vendedor) VALUES (?, ?, ?, ?)", (produto.get_nome(), produto.get_preco(), produto.get_empresa(), produto.get_numero()))
                conn.commit()
                print("Produto inserted successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error inserting produto: {e}")
            finally:
                self._close(conn)

    def alterar_produto(self, produto_id, nome=None, preco=None, quantidade=None):
        """Updates an existing product in the produto table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL UPDATE statement
                updates = []
                values = []
                if nome is not None:
                    updates.append("nome = ?")
                    values.append(nome)
                if preco is not None:
                    updates.append("preco = ?")
                    values.append(preco)
                if quantidade is not None:
                    updates.append("quantidade = ?")
                    values.append(quantidade)

                if not updates:
                    print("No fields to update.")
                    return

                sql = f"UPDATE produto SET {', '.join(updates)} WHERE id = ?"
                values.append(produto_id)

                cursor.execute(sql, tuple(values))
                conn.commit()
                print("Produto updated successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error updating produto: {e}")
            finally:
                self._close(conn)

    def deletar_produto(self, produto_id):
        """Deletes a product from the produto table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL DELETE statement
                cursor.execute("DELETE FROM produto WHERE id = ?", (produto_id,))
                conn.commit()
                print("Produto deleted successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error deleting produto: {e}")
            finally:
                self._close(conn)

    def selecionar_vendedor(self):
        """Selects all products from the produto table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL SELECT statement
                cursor.execute("SELECT * FROM vendedor")
                vendedores = cursor.fetchall()
                obj_vendedores = []
                for vendedores in vendedores:
                    obj_vendedor = Vendedor(vendedores[0], vendedores[1], vendedores[2]) 
                    obj_vendedores.append(obj_vendedor) 

                return obj_vendedores
                # Return the fetched products
            except Exception as e:
                print(f"Error selecting vendedores: {e}")
            finally:
                self._close(conn)

    def inserir_vendedor(self, vendedor: Type[Vendedor]):
        """Inserts a new seller into the vendedor table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL INSERT statement
                cursor.execute("INSERT INTO vendedor (nome, empresa) VALUES (?, ?)", (vendedor.get_nome(), vendedor.get_empresa()))
                conn.commit()
                print("Vendedor inserted successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error inserting vendedor: {e}")
            finally:
                self._close(conn)

    def alterar_vendedor(self, vendedor_id, nome=None, email=None, telefone=None):
        """Updates an existing seller in the vendedor table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL UPDATE statement
                updates = []
                values = []
                if nome is not None:
                    updates.append("nome = ?")
                    values.append(nome)
                if email is not None:
                    updates.append("email = ?")
                    values.append(email)
                if telefone is not None:
                    updates.append("telefone = ?")
                    values.append(telefone)

                if not updates:
                    print("No fields to update.")
                    return

                sql = f"UPDATE vendedor SET {', '.join(updates)} WHERE id = ?"
                values.append(vendedor_id)

                cursor.execute(sql, tuple(values))
                conn.commit()
                print("Vendedor updated successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error updating vendedor: {e}")
            finally:
                self._close(conn)

    def deletar_vendedor(self, vendedor_id):
        """Deletes a seller from the vendedor table."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                # Replace with your SQL DELETE statement
                cursor.execute("DELETE FROM vendedor WHERE id = ?", (vendedor_id,))
                conn.commit()
                print("Vendedor deleted successfully.")
            except Exception as e:
                conn.rollback()
                print(f"Error deleting vendedor: {e}")
            finally:
                self._close(conn)

    def selecionar_vendedor_com_maior_valor_produtos(self):
        """Finds the seller with the highest total product value."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vendedor.Numero_V, vendedor.Nome, vendedor.Empresa, SUM(produto.Preco) AS total_valor
                    FROM vendedor, produto
                    WHERE vendedor.Numero_V = produto.Vendedor
                    GROUP BY vendedor.Numero_V, vendedor.Nome, vendedor.Empresa
                    ORDER BY total_valor 
                """)
                resultado = cursor.fetchone()
                if resultado:
                    id = resultado[0]
                    nome = resultado[1]
                    empresa = resultado[2]
                    return Vendedor( nome, id, empresa)
                else:
                    print("No vendedores found.")
            except Exception as e:
                print(f"Error selecting vendedor with highest product value: {e}")
            finally:
                self._close(conn)

    def selecionar_valor_venda(self):
        """Finds the seller with the highest total product value."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vendedor.Numero_V, SUM(produto.Preco) AS total_valor
                    FROM vendedor, produto
                    WHERE vendedor.Numero_V = produto.Vendedor
                    GROUP BY vendedor.Numero_V, vendedor.Nome, vendedor.Empresa
                    ORDER BY total_valor 
                """)
                resultado = cursor.fetchone()
                if resultado:
                    soma = resultado[1]
                    return soma
                else:
                    print("No vendedores found.")
            except Exception as e:
                print(f"Error selecting vendedor with highest product value: {e}")
            finally:
                self._close(conn)
    
    def selecionar_produto_por_vendedor(self, vendedor_id):
        """Selects products by a specific seller."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM produto WHERE vendedor = ?", (vendedor_id,))
                produtos = cursor.fetchall()
                obj_produtos = []
                for produtos in produtos:
                    obj_produto = Produto(produtos[1], produtos[3], produtos[2], produtos[0], produtos[4])  # Adjust indices based on your table structure
                    obj_produtos.append(obj_produto)
                return obj_produtos
            except Exception as e:
                print(f"Error selecting products by vendedor: {e}")
            finally:
                self._close(conn)
    
    def selecionar_vendedor_valor(self):
        """Selects all sellers with their total product value."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT vendedor.Numero_V, vendedor.Nome, vendedor.Empresa, SUM(produto.Preco) AS total_valor
                    FROM vendedor, produto
                    WHERE vendedor.Numero_V = produto.Vendedor
                    GROUP BY vendedor.Numero_V, vendedor.Nome, vendedor.Empresa
                """)
                vendedores = cursor.fetchall()
                obj_vendedores = []
                for vendedores in vendedores:
                    obj_vendedor = Vendedor(vendedores[1], vendedores[0], vendedores[2]), vendedores[3]  # Adjust indices based on your table structure
                    obj_vendedores.append(obj_vendedor)
                return obj_vendedores
            except Exception as e:
                print(f"Error selecting vendedores with total value: {e}")
            finally:
                self._close(conn)

    def selecionar_maior_venda(self, vendedor: Type[Vendedor]):
        """Selects the highest sale value."""
        conn = self._connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT produto.Nome, produto.Empresa, produto.Vendedor, produto.Numero, MAX(produto.Preco) AS maior_venda
                    FROM produto
                    WHERE produto.Vendedor = ?
                    GROUP BY produto.Nome, produto.Empresa, produto.Vendedor, produto.Numero
                """, (vendedor.get_numero(),))
                resultado = cursor.fetchone()
                nome = resultado[0]
                empresa = resultado[1]
                vendedor_id = resultado[2]
                numero = resultado[3]
                preco = resultado[4]
                obj_produto = Produto (nome, preco, empresa, vendedor_id, numero)
                if resultado:
                    return obj_produto
                else:
                    print("No vendas found.")
            except Exception as e:
                print(f"Error selecting highest sale value: {e}")
            finally:
                self._close(conn)
    
    # Example usage (uncomment and modify as needed)
    # if __name__ == "__main__":
    #     db = Banco_de_Dados("your_database.db") # Replace with your database file/connection string
    
    #     # Example Insert
    #     # db.inserir_produto("Laptop", 1200.00, 10)
    #     # db.inserir_vendedor("John Doe", "john.doe@example.com", "123-456-7890")
    
    #     # Example Update
    #     # db.alterar_produto(1, preco=1150.00)
    #     # db.alterar_vendedor(1, email="jdoe@example.com")
      #     # Example Delete#     # db.deletar_produto(2)#     # db.deletar_vendedor(2)