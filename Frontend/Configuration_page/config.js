// Event-Listener für den "Start Simulation"-Button
document.getElementById("startSimulation").addEventListener("click", function (e) {
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

    config = [numb_robots, max_packages, battery, usage, capacity, sim_speed]
    
        // Asynchronous function to send POST request with JSON data
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
    console.log("CONFIGURATION")
    console.log(config)
    console.log(JSON.stringify(config))
    sendJSONStringWithPOST(url, JSON.stringify(config))

    // Weiterleitung zur Simulation-Seite
    window.location.href = "../Simulation_page/simulation.html";
});
