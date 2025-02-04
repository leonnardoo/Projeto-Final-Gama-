import pyodbc
import pandas as pd

class Database(object):
    conn = ""
    cursor = ""

    def __init__(self):
        self.connectDatabase()

    def connectDatabase(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   #'Server=LOCALHOST;'
                                   #'Database=BD_PROJETO_FINAL_COVID;'
                                   #'UID=sa;'
                                   #'PWD=sa;'
                                   'Server=dataheroes.database.windows.net;'
                                   'Database=Projeto_Final;'
                                   'UID=XXX;' #Usuario
                                   'PWD=XXX;' #Senha
        )
        self.cursor = self.conn.cursor()

    def closeConnexionDatabase(self):
        self.conn.close()

    def executeDatabase(self, query):
        exec_query = query
        self.cursor.execute(exec_query)
        self.cursor.commit()

    def showQuery(self, sql):
        return pd.read_sql(sql, self.conn)
