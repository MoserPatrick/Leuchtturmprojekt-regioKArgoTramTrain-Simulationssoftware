// Roboter-Daten laden
let robots = JSON.parse(localStorage.getItem('robots')) || [];

// Beispiel: Alle Roboter anzeigen
robots.forEach(robot => {
    console.log(`Roboter ${robot.id} hat ${robot.currentLoad} Pakete und ${robot.battery}% Batterie.`);
});