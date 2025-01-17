// Event-Listener für den "Start Simulation"-Button
document.getElementById("startSimulation").addEventListener("click", async function (e) {
    e.preventDefault();

    // Parameter aus den Eingabefeldern erfassen
    const numb_robots = document.getElementById('robots').value;
    const max_packages = document.getElementById('packages').value;
    const battery = document.getElementById('battery').value;
    const capacity = document.getElementById('capacity').value;
    const sim_speed = document.getElementById('speed').value;
    const usage = document.getElementById('energy').value;

    // Send Data to database
    url = "http://127.0.0.1:5000/config"

    config_array = [numb_robots, max_packages, battery, capacity, sim_speed, usage]

    const config_obj = {
        numb_robots: numb_robots,
        max_packages: max_packages,
        battery: battery,
        capacity: capacity,
        sim_speed: sim_speed,
        usage: usage
      };
    
        // Asynchronous function to send POST request with JSON data
    
    console.log("CONFIGURATION")
    await sendJSONStringWithPOST(url, JSON.stringify(config_array))
    // create initial robots
    url_start_sim = "http://127.0.0.1:5000/start_sim"
    await sendJSONStringWithPOST(url_start_sim, JSON.stringify(config_obj))

    // Weiterleitung zur Simulation-Seite
    //window.location.href = "../Simulation_page/simulation.html";
    //window.location.replace("../Simulation_page/simulation.html");
});

async function sendJSONStringWithPOST(url, jsonString) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'  // This is crucial to tell the server we are sending JSON
            },
            body: jsonString  // Sending the raw JSON string
        });

        // Wait for the response and parse it as JSON
        const data = await response.json();  // This will be the response data from the server

        console.log('Response:', data);  // Handle the server response here
    } catch (error) {
        console.error('Error:', error);  // Catch and log any error
    }
  }