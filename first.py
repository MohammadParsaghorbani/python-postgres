import psycopg2

conn = psycopg2.connect(host = 'localhost', port = '5432', user = 'postgres',database="test", password ='mparsa2010')
cur = conn.cursor()
conn.set_session(autocommit= True)

cur.execute("""

create table if not exists info(
    name varchar(20),
    last_name varchar(20),
    age int
);
""")
# cur.execute("""
# insert into info values('majid','ghorbani',40)
# """)
cur.execute("""
select * from info
""")
a = cur.fetchall()
for i in a:
    print(i)
# cur.execute("""
# create database test
# """)