import psycopg2
from ..settings import DB_CONFIG

conn = psycopg2.connect(user=DB_CONFIG['user'],
                        password=DB_CONFIG['password'],
                        port=DB_CONFIG['port'],
                        host=DB_CONFIG['host'],
                        dbname=DB_CONFIG['dbname'])

class BaseRepo():
    def __get_cursor(cls):
         return conn.cursor()
    def ping_tables(cls):
        #cur = cls.__get_cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cats;")
        print(cur.fetchall())
    
    def get_cats():
        cur = conn.cursor()
        cur.execute("SELECT * FROM cats;")
        print(cur.fetchall())


    def create_cat(name, color, tail_length, whiskers_length):
        cur = conn.cursor()
        cur.execute("INSERT INTO cats(name, color, tail_length, whiskers_length) VALUES (%s%s%s%s)", (name, color, tail_length, whiskers_length))


    def delete_cat(name):
        cur = conn.cursor()
        cur.execute("DELETE FROM cats WHERE name=(%s)", (name))


    def update_cat(name):
        cur = conn.cursor()
        cur.execute("UPDATE cats SET tail_length = '123' WHERE name = (%s)", (name))

baseRepo = BaseRepo()
#baseRepo.ping_tables()
baseRepo.create_cat(name="Musya", color="ginger", tail_length=100, whiskers_length=5)