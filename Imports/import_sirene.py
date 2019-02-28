import sqlite3
import csv
conn = sqlite3.connect('data.db')
c= conn.cursor()

with open('sirenerecode.csv', newline='') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='\"')
    for row in spamreader :
        if "\"" in row[2] :  
            recode=row[2].replace("\"", " ")
            requete = "INSERT INTO SIRENE VALUES("
            requete += "\""+row[0]+"\",\""+row[1]+"\",\""+recode+"\",\""+row[24]+"\",\""+row[27]+"\",\""+row[36]+"\",\""+row[42]+"\",\""+row[60]+"\",\""+row[61]+"\")"
        else :
            requete = "INSERT INTO SIRENE VALUES("
            requete += "\""+row[0]+"\",\""+row[1]+"\",\""+row[2]+"\",\""+row[24]+"\",\""+row[27]+"\",\""+row[36]+"\",\""+row[42]+"\",\""+row[60]+"\",\""+row[61]+"\")"
        #print(requete)        
        c.execute(requete)
conn.commit()
conn.close()

