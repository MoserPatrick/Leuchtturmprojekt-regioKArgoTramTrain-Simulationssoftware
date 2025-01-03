// Werte aus dem Local Storage abrufen
let robots = JSON.parse(localStorage.getItem('robots'));
let packages = localStorage.getItem('packages');

// Beispielausgabe in der Konsole
console.log(robots); // Array mit Roboter-Objekten
console.log(`Packages: ${packages}`);



