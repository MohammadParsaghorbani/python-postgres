import psycopg2

conn = psycopg2.connect(host = 'localhost', port = '5432', user = 'postgres',database="test", password ='mparsa2010')
cur = conn.cursor()
conn.set_session(autocommit= True)

cur.execute("""

create table info(
    name varchar(20),
    last_name varchar(20),
    age int
);
""")

# cur.execute("""
# create database test
# """)