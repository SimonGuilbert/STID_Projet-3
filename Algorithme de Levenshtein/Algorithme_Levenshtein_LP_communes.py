### Fonction Levenshtein ###
def levenshtein(mot1,mot2):
    ligne_i = [ k for k in range(len(mot1)+1)]
    for i in range(1, len(mot2) + 1):
        ligne_prec = ligne_i
        ligne_i = [i]*(len(mot1)+1)
        for k in range(1,len(ligne_i)):
            cout = int(mot1[k-1] != mot2[i-1])
            ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
    return ligne_i[len(mot1)]

### Code python ###

import sqlite3

conn = sqlite3.connect('data.db')
c_LP = conn.cursor()


for row_LP in c_LP.execute('SELECT * FROM LP WHERE q6_9a IS NOT NULL AND q6_9c IS NOT NULL'):
    c_communes = conn.cursor()
    distanceMinimum=1000
    requete = 'SELECT * FROM communes where departement = \'' + row_LP[4] + '\''
    for row_communes in c_communes.execute(requete):
        ville_lp = row_LP[6].lower()
        ville_lp = ville_lp.strip()
        ville_lp = ville_lp.replace("-", " ")
        ville_com = row_communes[2].lower()
        ville_com = ville_com.replace("-", " ")
        if ville_lp in ['cherbourg', 'octeville']:
            ville_lp = 'cherbourg octeville'
        elif ville_lp in ['beaumont', 'la hague']:
            ville_lp = 'beaumont hague'
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


