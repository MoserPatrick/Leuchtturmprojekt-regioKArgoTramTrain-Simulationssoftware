// Roboter-Daten laden
let robots = JSON.parse(localStorage.getItem('robots')) || [];

// Alle Roboter anzeigen
robots.forEach(robot => {
    console.log(`Roboter ${robot.id} hat ${robot.currentLoad} Pakete und ${robot.battery}% Batterie.`);
});