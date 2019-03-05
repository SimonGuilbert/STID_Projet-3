import csv
import random
f = open('Leaflet_MASTER.html', 'r+')
f.write('''<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.4.0/dist/leaflet.css"/>
        <script type="text/javascript" src="https://unpkg.com/leaflet@1.4.0/dist/leaflet.js"></script>
        <script type="text/javascript" src="leaflet-color-markers"></script>
    </head>
 
    <body onload="initialize()">
    <div id="map" style="width:100%; height:100%"></div>
        
<script>
    function initialize() {
        var map = L.map('map').setView([48.833, 2.333], 6);
 
        var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
            attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 19
        });
        map.addLayer(osmLayer);
''')
ville_prec = " " 
with open('Jointure_MASTER.csv', newline = '') as csvfile:
    csvfile.readline()
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')
    for row in spamreader:
        if row[10] != "":
            nom_entreprise = row[7]
            if nom_entreprise == "":
                nom_entreprise = "Inconnu"
            #if row[9] == ville_prec :
            lon = float(row[11]) + random.uniform(-0.02, 0.02)
            lat = float(row[10]) + random.uniform(-0.02, 0.02)
            lat = str(lat)
            lon = str(lon)
            f.write('L.marker(['+lat+','+lon+']).addTo(map).bindPopup('+'\"<b>'+row[9]+'</b>,<br>'+nom_entreprise+'\"'+');'+'\n')
            #else :
                #lon = row[11]
                #lat = row[10]
                #f.write('L.marker(['+lat+','+lon+']).addTo(map).bindPopup('+'\"<b>'+row[9]+'</b>,<br>'+nom_entreprise+'\"'+');'+'\n')
            #ville_prec = row[9]

f.write('''
    } 
</script>    
</body>
</html>
''')
f.close()
