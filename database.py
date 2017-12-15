import psycopg2
from psycopg2 import pool

def connect():
    return psycopg2.connect(user='learnadmin', password = 'Hi5Michael', database='SnapshotDev', host='snapshotdev.cpeg0owf2zfo.us-west-2.rds.amazonaws.com')


class Database():
    __connection_pool = None

    @staticmethod
    def initialize(cls, **kwargs):
        Database.connection_pool = pool.SimpleConnectionPool(1,
                                                             10,
                                                             # the below arguments can be passed in another function
                                                             database="",
                                                             user="",
                                                             password="",
                                                             host="")

    @classmethod
    def get_connection(cls):
        return cls.connection.getconn()

    @classmethod
    def return_connection(cls, connection):
        return Database.connection_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls):
        return Database.connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)