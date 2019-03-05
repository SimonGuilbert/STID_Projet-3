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


for row_LP in c_LP.execute('SELECT * FROM LP WHERE q6_14_6 IS NOT NULL'):
    c_sirene = conn.cursor()
    distanceMinimum=1000
    requete = 'SELECT * FROM SIRENE WHERE DEPET = \'' + row_LP[4] + '\''
    for row_sirene in c_sirene.execute(requete):

        nom_etablissement_LP = row_LP[7].lower()
        nom_etablissement_LP = nom_etablissement_LP.strip()
        nom_etablissement_LP = nom_etablissement_LP.replace("-", " ")
        nom_etablissement_LP = nom_etablissement_LP.replace("\'", " ")

        L1_NORMALISEE_sirene = row_sirene[2].lower()
        L1_NORMALISEE_sirene = L1_NORMALISEE_sirene.strip()
        L1_NORMALISEE_sirene = L1_NORMALISEE_sirene.replace("-", " ")

        ENSEIGNE_sirene = row_sirene[5].lower()
        ENSEIGNE_sirene = ENSEIGNE_sirene.strip()
        ENSEIGNE_sirene = ENSEIGNE_sirene.replace("-", " ")

        NOMEN_LONG_sirene = row_sirene[7].lower()
        NOMEN_LONG_sirene = NOMEN_LONG_sirene.strip()
        NOMEN_LONG_sirene = NOMEN_LONG_sirene.replace("-", " ")

        SIGLE_sirene = row_sirene[8].lower()
        SIGLE_sirene = SIGLE_sirene.strip()
        SIGLE_sirene = SIGLE_sirene.replace("-", " ")

        if levenshtein(nom_etablissement_LP, L1_NORMALISEE_sirene) < distanceMinimum :
            distanceMinimum = levenshtein(nom_etablissement_LP, L1_NORMALISEE_sirene)
            SIREN = row_sirene[0]
            NIC = row_sirene[1]
            NOM_ETAB = row_sirene[2]
            APET700 = row_sirene[6]

        if levenshtein(nom_etablissement_LP, ENSEIGNE_sirene) < distanceMinimum :
            distanceMinimum = levenshtein(nom_etablissement_LP, ENSEIGNE_sirene)
            SIREN = row_sirene[0]
            NIC = row_sirene[1]
            NOM_ETAB = row_sirene[5]
            APET700 = row_sirene[6]

        if levenshtein(nom_etablissement_LP, NOMEN_LONG_sirene) < distanceMinimum :
            distanceMinimum = levenshtein(nom_etablissement_LP, NOMEN_LONG_sirene)
            SIREN = row_sirene[0]
            NIC = row_sirene[1]
            NOM_ETAB = row_sirene[7]
            APET700 = row_sirene[6]

        if levenshtein(nom_etablissement_LP, SIGLE_sirene) < distanceMinimum :
            distanceMinimum = levenshtein(nom_etablissement_LP, SIGLE_sirene)
            SIREN = row_sirene[0]
            NIC = row_sirene[1]
            NOM_ETAB = row_sirene[8]
            APET700 = row_sirene[6]

    if distanceMinimum < 3:
        requete = 'UPDATE LP SET SIREN = \'' + SIREN + '\', '
        requete += 'NIC = \'' + NIC + '\', NOM_ETAB = \'' + NOM_ETAB + '\', APET700 = \'' + APET700 + '\''
        #print(requete)
        c_sirene.execute(requete)
     
conn.commit()
conn.close()
