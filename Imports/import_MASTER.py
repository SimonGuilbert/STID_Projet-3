import sqlite3
import csv
conn = sqlite3.connect('data.db')
c= conn.cursor()
with open('dataBrutes_MASTER.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
    for row in spamreader :
        requete = "INSERT INTO MASTER VALUES("
        for i in range(8):
            valeur=row[i].strip()
            if valeur=="":
                requete += "NULL,"
            else:
                requete += "\""+row[i].strip()+"\","
        requete = requete[:-1] + ")"
        #c.execute(requete)
        print(requete)
conn.commit()
conn.close()
