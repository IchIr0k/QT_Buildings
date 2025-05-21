import sqlite3

class Sale:
    def __init__(self):
        self.con = sqlite3.connect("Building_.db")
        self.cur = self.con.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS Sale (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_of_structure INTEGER NOT NULL,
                num_of_rooms INTEGER NOT NULL,
                Footage REAL NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (type_of_structure) REFERENCES Structure(id_building)
            )
        ''')
        self.con.commit()

    def __del__(self):
        self.con.close()

    def view(self):
        self.cur.execute("SELECT * FROM Sale")
        return self.cur.fetchall()

    def view_with_type(self):
        self.cur.execute('''
            SELECT Sale.id, Structure.type_of_structure, Sale.num_of_rooms, Sale.Footage, Sale.price
            FROM Sale
            JOIN Structure ON Sale.type_of_structure = Structure.id_building
        ''')
        return self.cur.fetchall()

    def insert(self, type_id, num_of_rooms, footage, price):
        self.cur.execute("INSERT INTO Sale (type_of_structure, num_of_rooms, Footage, price) VALUES (?, ?, ?, ?)",
                         (type_id, num_of_rooms, footage, price))
        self.con.commit()
