import psycopg2
from faker import Faker

# conexao com bd
con = psycopg2.connect(
    host='localhost',
    database='pycodebr',
    user='postgres',
    password='cvrs'
)
cur = con.cursor()

# lib FAKER em pt-br
fake = Faker(locale='pt-br')

base_sql = '''
    INSERT INTO seguidores
        (nome, email, usuario)
    VALUES
        ('{}', '{}', '{}')
    '''

# cria 1000 registro
for i in range(1000):
    nome = fake.name()
    email = fake.email()
    usuario = fake.user_name()
    sql = base_sql.format(nome, email, usuario)
    cur.execute(sql)

# faz commit no banco e encerra a conexao
con.commit()
con.close()