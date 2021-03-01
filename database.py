import sqlite3


class Database:
    def __init__(self, database_name):
        self.connect = sqlite3.connect(database_name)

    def save(self, login, password, board):
        board = [[str(el) for el in elem] for elem in board]
        board = '/'.join([' '.join(elem) for elem in board])
        cur = self.connect.cursor()
        id = cur.execute(f"""SELECT id FROM users
                                WHERE login='{login}' and password='{password}'""")
        cur.execute(f"""UPDATE saves
                        SET board='{board}'
                        WHERE id={id}""")
        self.connect.commit()

    def open(self, login, password):
        cur = self.connect.cursor()
        id = cur.execute(f"""SELECT id FROM users
                                    WHERE login='{login}' and password='{password}'""")
        board = cur.execute(f"""SELECT board FROM saves
                                    WHERE id={id}""")
        self.connect.commit()
        board = [[int(el) for el in elem.split(' ')]for elem in board[0].split('/')]
        return board

    def register(self, login, password):
        cur = self.connect.cursor()
        cur.execute(f"""INSERT INTO users(login,password) VALUES ('{login}','{password}')""")
        id = cur.execute(f"""SELECT id FROM users
                                WHERE login='{login}' and password='{password}'""")
        cur.execute(f"""INSERT INTO saves(id,password) VALUES ({id},'')""")
        self.connect.commit()

    def close(self):
        self.connect.close()
