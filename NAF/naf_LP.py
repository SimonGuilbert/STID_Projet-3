import sqlite3

conn = sqlite3.connect('data.db')
c_LP = conn.cursor()


for row_LP in c_LP.execute('SELECT * FROM LP WHERE APET700 IS NOT NULL'):
    c_naf = conn.cursor()
    requete = 'SELECT * FROM NAF where NIV5 = \'' + row_LP[15] + '\''
    for row_naf in c_naf.execute(requete):
        requete = 'UPDATE LP SET NIV1 = \'' + row_naf[1] + '\' WHERE CODE = \'' + row_LP[0] + '\''
        print(requete)
        #c_naf.execute(requete)
     
conn.commit()
conn.close()
