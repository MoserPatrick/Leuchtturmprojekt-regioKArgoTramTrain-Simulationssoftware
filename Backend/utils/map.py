import folium

# Koordinaten für Karlsruhe Map an sich
karlsruhe_coords = [49.0069, 8.4037]

# Karte erstellen
karte = folium.Map(location=karlsruhe_coords, zoom_start=13)

# Haltestellen für Karlsruhe
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

# Straßenbahnlinien (Verbindungen zwischen den Haltestellen)
linien = [
    {"name": "Linie 1", "path": [[48.9937, 8.4010], [49.0097, 8.4044], [49.0092, 8.3923]]},
    {"name": "Linie 2", "path": [[48.9937, 8.4010], [48.9992, 8.4655]]},
]

# Linien auf der Karte einzeichnen
for linie in linien:
    folium.PolyLine(
        locations=linie["path"],
        color="red",
        weight=5,
        popup=linie["name"]
    ).add_to(karte)

# Karte als HTML speichern
karte.save("karlsruhe_bahnnetz.html")
