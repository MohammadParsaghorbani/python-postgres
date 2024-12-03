import psycopg2

conn = psycopg2.connect(host = 'localhost', port = '5432', user = 'postgres',database="test", password ='mparsa2010')
cur = conn.cursor()
conn.set_session(autocommit= True)

while True:
    try:
        option = int(input("option :\n\t1) add data\n\t2) read data\n\t3) update data\n\t4) remove data\n:"))
        break
    except ValueError:
        print("wrong option!")