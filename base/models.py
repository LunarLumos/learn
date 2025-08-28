import sqlite3

class ProductDB:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        conn = self.connect()
        conn.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT)"
        )
        conn.commit()
        conn.close()

    def add_product(self, name):
        conn = self.connect()
        conn.execute("INSERT INTO products (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    def remove_product(self, product_id):
        conn = self.connect()
        conn.execute("DELETE FROM products WHERE id=?", (product_id,))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = self.connect()
        cursor = conn.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows
