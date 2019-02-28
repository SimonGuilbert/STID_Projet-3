import sqlite3
import csv
conn = sqlite3.connect('data.db')
c= conn.cursor()

with open('sirenerecode.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
    for row in spamreader :
        requete = "INSERT INTO SIRENE VALUES("
        requete += "\""+row[0]+"\",\""+row[1]+"\",\""+row[2].replace("\"", " ")+"\",\""+row[24]+"\",\""+row[27]+"\",\""+row[36]+"\",\""+row[42]+"\",\""+row[60]+"\",\""+row[61]+"\")"
        #print(requete)        
        c.execute(requete)
conn.commit()
conn.close()

