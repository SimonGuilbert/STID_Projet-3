import sqlite3

conn = sqlite3.connect('data.db')
c_MASTER = conn.cursor()


for row_MASTER in c_MASTER.execute('SELECT * FROM MASTER WHERE APET700 IS NOT NULL'):
    c_naf = conn.cursor()
    requete = 'SELECT * FROM NAF where NIV5 = \'' + row_MASTER[15] + '\''
    for row_naf in c_naf.execute(requete):
        requete = 'UPDATE MASTER SET NIV1 = \'' + row_naf[1] + '\' WHERE CODE = \'' + row_MASTER[0] + '\''
        #print(requete)
        c_naf.execute(requete)
    
conn.commit()
conn.close()
