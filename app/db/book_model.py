import psycopg2
import os
def connect_to_db():
    host = os.getenv("DATABASE_HOST")
    database = os.getenv("DATABASE_NAME")
    user = os.getenv("DATABASE_USER")
    password = os.getenv("DATABASE_PASSWORD")
    port = os.getenv("DATABASE_PORT")
    
    try:
        conn = psycopg2.connect(host=host,database=database,user=user,password=password,port=port)
        # cur = conn.cursor()
        # command = """
        # CREATE TABLE books (
        #         book_id INTEGER PRIMARY KEY,
        #         book_name VARCHAR(100) NOT NULL,
        #         book_author VARCHAR(100) NOT NULL,
        #         book_price VARCHAR(100) NOT NULL,
        #         book_url VARCHAR(100) NOT NULL,
        #         book_image VARCHAR(100) NOT NULL       
        # )
        # """
        # command = """
        # SELECT * from books
        # """
        # command = """
        # ALTER TABLE books ALTER COLUMN book_id SET INTEGER PRIMARY KEY SERIAL
        # """
        # a = cur.execute(command)
        # print("Table Created")
        return conn
    except Exception as e:
        print(e)


class BookModel():
    def __init__(self, *kwargs):
        self.book_id = kwargs[0]
        self.book_name = kwargs[1]
        self.book_author = kwargs[2]
        self.book_price = kwargs[3]
        self.book_url = kwargs[4]
        self.book_image = kwargs[5]

    @staticmethod
    def get_all_books():
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            command = "SELECT * from books"
            cur.execute(command)
            resarr = cur.fetchall()
            finalarr = []
            if resarr:
                for i in resarr:
                    bo = BookModel(*i)
                    finalarr.append(bo.__dict__)
            return finalarr
        except:
            return None

    @classmethod
    def get_book_by_id(cls, id):
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            command = "SELECT * from books where book_id="+str(id)
            cur.execute(command)
            resarr = cur.fetchone()
            finalarr = []
            if resarr:
                bo = cls(*resarr)
                finalarr.append(bo.__dict__)
            return finalarr
        except:
            return None

    @staticmethod
    def insert_book(deftupleval):
        insert_query = "INSERT INTO books (book_name,book_author,book_price,book_url,book_image) VALUES(%s,%s,%s,%s,%s)"
        tupleval = deftupleval
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute(insert_query,deftupleval)
            conn.commit()
            return True
        except:
            return None

    @staticmethod
    def delete_books():
        delete_query = "delete from books"
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute(delete_query)
            conn.commit()
            return True
        except:
            return None

    @staticmethod
    def delete_book_by_id(id):
        delete_query = "delete from books where book_id=%s"
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute(delete_query,(id,))
            conn.commit()
            return True
        except:
            return None

    @staticmethod
    def update_book(deftupleval):
        insert_query = "UPDATE books set book_name=%s , book_author=%s, book_price=%s, book_url=%s,book_image=%s where book_id=%s"
        try:
            conn = connect_to_db()
            cur = conn.cursor()
            cur.execute(insert_query,deftupleval)
            conn.commit()
            return True
        except:
            return None
