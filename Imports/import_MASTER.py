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
              requete += "\""+row[i]+"\","
        requete = requete[:-1] + ")"
        c.execute(requete)
conn.commit()
conn.close()

