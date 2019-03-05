import sqlite3
conn = sqlite3.connect('data.db')
c_LP = conn.cursor()
for row_LP in c_LP.execute('SELECT * FROM LP WHERE q6_9a IS NOT NULL AND q6_9c IS NOT NULL'):
    c_naf = conn.cursor()
    distanceMinimum=1000
    requete = 'SELECT * FROM communes where departement = \'' + row_LP[4] + '\''
    for row_communes in c_communes.execute(requete):
        if levenshtein(ville_lp, ville_com) < distanceMinimum:
            distanceMinimum = levenshtein(ville_lp, ville_com)
            code_insee = row_communes[0]
            nom_commune = row_communes[2].replace('\'', '\'\'')
            latitude = str(row_communes[4])
            longitude = str(row_communes[3])
    if distanceMinimum < 3:
        requete = 'UPDATE LP SET CODE_INSEE = \'' + code_insee + '\', '
        requete += 'LATITUDE = ' + latitude + ', LONGITUDE = ' + longitude + ', '
        requete += 'NOM_COM = \'' + nom_commune + '\' WHERE CODE = \'' + row_LP[0] + '\''
        # print(row_LP[0], row_LP[6], nom_commune, distanceMinimum, sep=",")
        # print(requete)
        #c_communes.execute(requete)
      
conn.commit()
conn.close()
