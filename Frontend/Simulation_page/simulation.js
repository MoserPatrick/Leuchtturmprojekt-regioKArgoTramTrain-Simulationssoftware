import { simulationTimer } from './simulationTimer.js';

const timer = new simulationTimer();
const config = get_config()
  
// Simulate time advancing every second
const simulationInterval = setInterval(() => {
  timer.advanceTime();
  console.log("Current Time:", timer.getCurrentTime());

  // Stop the simulation after one full cycle for demonstration
  if (timer.getCurrentTime() === "12:00") {
    clearInterval(simulationInterval);
    console.log("Simulation complete.");
  }
}, 1000 * config.speed); // Advance simulation every second


async function reset_sim(){
    // reset Time
    timer.stop()
    timer.reset()
    // delete database data
    url_config_delete = `http://127.0.0.1:5000/config/delete`
    url_robots_delete = `http://127.0.0.1:5000/robots/delete`
    delete_config(url_config_delete)
    delete_config(url_robots_delete)
    // go back to the configuration site
    window.location.href = "../Configuration_page/config.html";

}


// Function to send DELETE request
function delete_data(url) {
  fetch(url, {
    method: 'DELETE',  // HTTP method is DELETE
    headers: {
      'Content-Type': 'application/json',  // Set the request body as JSON
    },
  })
  .then(response => {
    if (response.ok) {
      console.log("Data deleted successfully!");
      return response.json();
    } else {
      throw new Error('Failed to delete data');
    }
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error("Error:", error);
  });
}
// Function to get Robot data
async function getRobotsData() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/robots`);  // Fetch robots data from Flask server
        const robotsData = await response.json();  // Parse the response as JSON

        if (response.ok) {
            const robotInstances = [];  // Array to store robot objects

            robotsData.forEach(robot => {
                const robotInstance = {
                    id: robot.id,
                    position: robot.position,
                    energy: robot.energy,
                    numb_packages: robot.numb_packages,
                    status: robot.status,
                    destination: robot.destination,
                    speed: robot.speed,
                    weight: robot.weight
                };

                robotInstances.push(robotInstance);  // Store robot object in the array
            });
            // How to get Attributes: RobotInsatnces[which one].attribute
        } else {
            console.log("Error:", robotsData.error);  // Handle any errors
        }
    } catch (error) {
        console.error("Error fetching robots data:", error);  // Catch and log any errors
    }
}

async function get_config() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/config`);  // Fetch robots data from Flask server
        const config_data = await response.json();  // Parse the response as JSON

        if (response.ok) {
            console.log[config_data]
            return config_data
        } else {
            console.log("Error:", config_data.error);  // Handle any errors
        }
    } catch (error) {
        console.error("Error fetching config data:", error);  // Catch and log any errors
    }
}

async function Robot_method(robot, url) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(robot) // Send the robot data as JSON
        });

        const data = await response.json();

        if (response.ok) {
            console.log('Robot data successfully posted:', data);
        } else {
            console.error('Error:', data.error);
        }
    } catch (error) {
        console.error('Request failed:', error);
    }
}

// Example usage
const url_charge_robot = `http://127.0.0.1:5000/robot/charge`;
const url_deliever_robot = `http://127.0.0.1:5000/robots/deliever`;
//Robot_method(robotInstances[2], url_charge_robot);  // Call the method for robot with ID 1
//Robot_method(robotInstances[2], url_deliever_robot);


// Beispielausgabe in der Konsole
//console.log(robots); // Array mit Roboter-Objekten
//console.log(`Packages: ${packages}`);



