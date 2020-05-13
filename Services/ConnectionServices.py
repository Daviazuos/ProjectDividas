import psycopg2
import configparser
from collections import namedtuple

class conn:
    def ConnPostgres(self):
        Conn = namedtuple("Conn", "cursor conn")
        Host, User, Passwd, Port, Db = conn.ConfigDB(self)
        con = psycopg2.connect(host=Host, database=Db, user=User, password=Passwd, port=Port)
        cur = con.cursor()
        return Conn(cur,con)

    def ConfigDB(self):
        DadosDb = configparser.ConfigParser()
        DadosDb.read('config.ini')

        host = DadosDb['POSTGRES DEV']['host']
        db = DadosDb['POSTGRES DEV']['db']
        User = DadosDb['POSTGRES DEV']['User']
        port = DadosDb['POSTGRES DEV']['port']
        password = DadosDb['POSTGRES DEV']['password']
        return host, User, password, port, db