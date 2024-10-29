# import sqlite3 as db


# with db.connect('noma.db') as con:
#     cur = con.execute("""CREATE TABLE "Tests2"(
#         id_produkts     INTEGER,
#         id_nomnieks     INTEGER,
#         sak_datums     TEXT,
#         beigu_datums     TEXT,
#         PRIMARY KEY(id_produkts, id_nomnieks)
#     )""")

# con.close()

import sqlite3 as db

with db.connect('noma.db') as con:
    cur = con.execute("""SELECT * FROM Nomnieks WHERE vards='Pēteris'""")
    nomnieki = cur.fetchall()
    for rinda in nomnieki:
        #print(f'Tavs ID nr.: {rinda[0]}; Tavs vārds: {rinda[1]}') #nestrada ar fetchone
        print(rinda) #ar type var redzet tipu (str, int, utt)
        print(rinda[1], ' ar personas kodu = ', rinda[4],'\n' )