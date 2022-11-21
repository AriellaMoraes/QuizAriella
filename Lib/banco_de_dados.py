import sqlite3 

#conectando...
DATABASE = 'Lib/database.db'
conn = sqlite3.connect(DATABASE, check_same_thread=False)

# definindo um cursor
cursor = conn.cursor()



def create_ranking():
    #criando uma tabela
    cursor.execute("""
    CREATE TABLE  IF NOT EXISTS Ranking(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    qtde_acertos INT,
    wrong_answers TEXT NOT NULL,
    user TEXT);
    """)

def insert_ranking(valores_campos):
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    cursor = conn.cursor()
    table_name = 'Ranking'
    
    nomes_campos = ('qtde_acertos','wrong_answers','user')
    sql_str = f'''INSERT INTO {table_name} {nomes_campos} VALUES {valores_campos};'''
    cursor.execute(sql_str)
    print(sql_str)
    conn.commit()
    conn.close()


create_ranking()
