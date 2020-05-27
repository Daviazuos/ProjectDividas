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

        host = DadosDb['HEROKU POSTGRES']['host']
        db = DadosDb['HEROKU POSTGRES']['db']
        User = DadosDb['HEROKU POSTGRES']['User']
        port = DadosDb['HEROKU POSTGRES']['port']
        password = DadosDb['HEROKU POSTGRES']['password']
        return host, User, password, port, db