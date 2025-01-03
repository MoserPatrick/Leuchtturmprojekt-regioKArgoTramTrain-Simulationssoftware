// Event-Listener für den "Start Simulation"-Button
document.getElementById("startSimulation").addEventListener("click", function (e) {
    e.preventDefault();

    // Parameter aus den Eingabefeldern erfassen
    const robots = document.getElementById('robots').value;
    const packages = document.getElementById('packages').value;
    const battery = document.getElementById('battery').value;
    const energy = document.getElementById('energy').value;
    const capacity = document.getElementById('capacity').value;
    const speed = document.getElementById('speed').value;

    // Roboter-Objekte erstellen und in ein Array packen
    let robotConfig = [];
    for (let i = 0; i < robots; i++) {
        robotConfig.push({
            id: i + 1,
            position: [0, 0], // Startposition 
            battery: parseFloat(battery),
            energyUsage: parseFloat(energy),
            loadCapacity: parseFloat(capacity),
            currentLoad: 0, // Anfangswert für Ladung
            speed: parseFloat(speed),
            target: null, // Ziel wird später gesetzt
            status: 'idle' // Status: idle, moving, loading
        });
    }

    // Parameter im Local Storage speichern
    localStorage.setItem('robots', JSON.stringify(robotConfig));
    localStorage.setItem('packages', packages);

    // Weiterleitung zur Simulation-Seite
    window.location.href = "../Simulation_page/simulation.html";
});
