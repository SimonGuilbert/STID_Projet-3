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
c_MASTER = conn.cursor()


for row_MASTER in c_MASTER.execute('SELECT * FROM MASTER WHERE q6_9a IS NOT NULL AND q6_9c IS NOT NULL'):
    c_communes = conn.cursor()
    distanceMinimum=1000
    requete = 'SELECT * FROM communes where departement = \'' + row_MASTER[4] + '\''
    for row_communes in c_communes.execute(requete):
        ville_MASTER = row_MASTER[6].lower()
        ville_MASTER = ville_MASTER.strip()
        ville_MASTER = ville_MASTER.replace("-", " ")
        ville_MASTER = ville_MASTER.replace("st ", "saint ")
        ville_com = row_communes[2].lower()
        ville_com = ville_com.replace("-", " ")
        if ville_MASTER in ['cherbourg', 'octeville']:
            ville_MASTER = 'cherbourg octeville'
        elif ville_MASTER in ['beaumont', 'la hague']:
            ville_MASTER = 'beaumont hague'
        if levenshtein(ville_MASTER, ville_com) < distanceMinimum:
            distanceMinimum = levenshtein(ville_MASTER, ville_com)
            code_insee = row_communes[0]
            nom_commune = row_communes[2].replace('\'', '\'\'')
            latitude = str(row_communes[4])
            longitude = str(row_communes[3])
    if distanceMinimum < 3:
        requete = 'UPDATE MASTER SET CODE_INSEE = \'' + code_insee + '\', '
        requete += 'LATITUDE = ' + latitude + ', LONGITUDE = ' + longitude + ', '
        requete += 'NOM_COM = \'' + nom_commune + '\' WHERE CODE = \'' + row_MASTER[0] + '\''
        #print(row_MASTER[0], row_MASTER[6], nom_commune, distanceMinimum, sep=",")
        #print(requete)
        c_communes.execute(requete)
      
conn.commit()
conn.close()
