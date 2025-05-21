import sqlite3

class Structure:
    def __init__(self):
        self.con = sqlite3.connect("Building_.db")
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Structure (
                id_building INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_structure TEXT NOT NULL
            )
        ''')
        self.con.commit()

    def __del__(self):
        self.con.close()

    def view(self):
        self.cur.execute("SELECT * FROM Structure")
        return self.cur.fetchall()

    def insert(self, type_of_structure):
        self.cur.execute("INSERT INTO Structure (type_of_structure) VALUES (?)", (type_of_structure,))
        self.con.commit()

    def search(self, type_of_structure):
        self.cur.execute("SELECT * FROM Structure WHERE type_of_structure = ?", (type_of_structure,))
        return self.cur.fetchall()
