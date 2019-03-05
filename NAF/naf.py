import sqlite3

conn = sqlite3.connect('data.db')
c_LP = conn.cursor()


for row_LP in c_LP.execute('SELECT * FROM LP WHERE APET700 IS NOT NULL'):
    c_naf = conn.cursor()
    requete = 'SELECT * FROM SIRENE where APET700 = \'' + row_naf[0] + '\''
    for row_naf in c_naf.execute(requete):
        NIV1 = row_naf[1]
        requete = 'UPDATE LP SET NIV1 = \'' + NIV1 + '\''
        print(requete)
        c_naf.execute(requete)
     
conn.commit()
conn.close()
