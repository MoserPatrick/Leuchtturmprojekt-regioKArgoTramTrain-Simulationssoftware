import folium

#Koordinaten für Karlsruhe Map an sich
karlsruhe_coords = [49.0069, 8.4037]

# Karte erstellen
karte = folium.Map(location=karlsruhe_coords, zoom_start=13)

# Haltestellenfür Karlsruhe (nur Beispieldaten bisher -> mal schauen, ob wir einfach direkt alle Spots angeben können)
haltestellen = [
    {"name": "Karlsruhe Hauptbahnhof", "coords": [48.9937, 8.4010]},
    {"name": "Marktplatz", "coords": [49.0097, 8.4044]},
    {"name": "Durlach Bahnhof", "coords": [48.9992, 8.4655]},
    {"name": "Europaplatz", "coords": [49.0092, 8.3923]},
]

# Haltestellen auf der Karte markieren
for haltestelle in haltestellen:
    folium.Marker(
        location=haltestelle["coords"],
        popup=haltestelle["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(karte)

# erstellt Karte als HTML-Datei (wir rufen die html-Datei in der Simulation auf)
karte.save("karlsruhe_bahnnetz.html")

