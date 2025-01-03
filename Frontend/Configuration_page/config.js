document.getElementById('config-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Parameter erfassen
    const numRobots = document.getElementById('robots').value;
    const numPackages = document.getElementById('packages').value;
    const battery = document.getElementById('battery').value;
    const energy = document.getElementById('energy').value;
    const capacity = document.getElementById('capacity').value;
    const speed = document.getElementById('speed').value;

    // Roboter-Objekte erstellen
    let robots = [];
    for (let i = 0; i < numRobots; i++) {
        robots.push({
            id: i + 1,
            position: [0, 0], // Startposition
            battery: parseFloat(battery),
            energyUsage: parseFloat(energy),
            loadCapacity: parseFloat(capacity),
            currentLoad: Math.floor(Math.random() * numPackages), // Zufällige Paketanzahl fürs testen
            speed: parseFloat(speed),
            target: null, // Zielstation
            status: 'idle', // Status: idle, moving, loading
        });
    }

    // Speichern in Local Storage (oder später POST an Backend)
    localStorage.setItem('robots', JSON.stringify(robots));

    // Weiter zur Simulation-Seite
    window.location.href = 'simulation.html';
});
