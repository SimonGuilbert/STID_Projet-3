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

seuil = 0.15
for row_LP in c_LP.execute('SELECT * FROM LP WHERE q6_14_6 IS NOT NULL AND CODE_INSEE IS NOT NULL'):
    print(row_LP[0])
    c_sirene = conn.cursor()
    distanceMinimum=1000
   
    if row_LP[8] not in [75056]:
        requete = 'SELECT * FROM SIRENE WHERE CODE_INSEE = \"' + str(row_LP[8]) + '\"'
    else:
        requete = 'SELECT * FROM SIRENE WHERE DEPET = \"' + str(row_LP[4]) + '\"'
    #print(requete)

    nom_etablissement_LP = row_LP[7].lower()
    nom_etablissement_LP = nom_etablissement_LP.strip()
    nom_etablissement_LP = nom_etablissement_LP.replace("-", " ")
    nom_etablissement_LP = nom_etablissement_LP.replace("\'", " ")

    for row_sirene in c_sirene.execute(requete):
        for i in [2,5,7,8]:
            Nom = row_sirene[i].lower()
            Nom = Nom.strip()
            Nom = Nom.replace("-", " ")

            if levenshtein(nom_etablissement_LP, Nom) < distanceMinimum :
                distanceMinimum = levenshtein(nom_etablissement_LP, Nom)
                SIREN = row_sirene[0]
                NIC = row_sirene[1]
                NOM_ETAB = row_sirene[2]
                APET700 = row_sirene[6]
        '''if distanceMinimum == 0:   
            print(nom_etablissement_LP, NOM_ETAB)       
            break
        '''
    if distanceMinimum < seuil * len(row_LP[7]) :
        requete = 'UPDATE LP SET SIREN = \"' + SIREN + '\", '
        requete += 'NIC = \"' + NIC + '\", NOM_ETAB = \"' + NOM_ETAB + '\", APET700 = \"' + APET700 + '\"'
        requete += ' WHERE CODE = \"' + row_LP[0] + '\"'
        # print(requete)
        c_sirene.execute(requete)
conn.commit()
conn.close()
