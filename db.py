import psycopg

from psycopg.rows import dict_row

class Database:
    
    conn = None

    def __init__(self):
        self.connect()

    def connect(self):
        if self.conn is None:
            self.conn = psycopg.connect(user='postgres', password='123456', host='172.17.0.1', dbname='blocks', row_factory=dict_row)

        return self.conn
    
    def query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor
    
    def close(self):
        self.conn.close()
