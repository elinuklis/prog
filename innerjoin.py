import sqlite3 as db 

with db.connect('noma.db') as con:
  cur = con.cursor()
  # izvelas vardus un uzvardus, arnoradito vardu 
  cur.execute(""" SELECT  Nomnieks.vards, Nomnieks.uzvards, Nomnieks.tel_nr, Noma.beig_datums
              FROM Nomnieks
              INNER JOIN Noma
              ON Noma.id_nomnieks = Nomnieks.id_nomnieks  """)
  nomniek = cur.fetchall()

print('Izdrukā nomnieku vārdus, uzvārdus, mob.nr, kad jāatdod produkts')
for rinda in nomniek:
  print (rinda)
