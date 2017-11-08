import psycopg2

class Conexao(object):


    def __init__(self):
        self.conn = psycopg2.connect("dbname=financeiro user=postgres")
        self.cur = self.conn.cursor()


    def ExecutaConsultaTodos(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def FechaConexao(self):
        self.cur.close()
        self.conn.close()