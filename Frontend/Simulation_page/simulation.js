import { simulationTimer } from './simulationTimer.js';


let timer = new simulationTimer();
if (!timer.running){
  timer.running = true;
}
//const config = get_config()
/*
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
*/




// creating the right Robot list
function create_robot_element(id) {
    console.log("creating robots");
    const image = 'images/Robot.png';
    const listItem = document.createElement('li');
    listItem.classList.add('single-roboter');
    listItem.innerHTML = `${id}. <img src="${image}" />`;
    return listItem;
  }

  const button = document.getElementById('cancel-simulation');
  if (button) {
    button.addEventListener('click', async function() {
      console.log("deleting!!");
      // reset Time
      if (timer) {
        timer.stop();
        timer.reset();
      }
      // delete database data
      const url_config_delete = `http://127.0.0.1:5000/config/delete`;
      const url_robots_delete = `http://127.0.0.1:5000/robots/delete`;
      await delete_data(url_config_delete);
      await delete_data(url_robots_delete);
      // go back to the configuration site
      console.log("Data deleted, redirecting...");
      //window.location.href = "../Configuration_page/config.html";
      window.location.replace("../Configuration_page/config.html");
    });
  } else {
    console.log("Cancel button not found!");
  }

  // Get the parent div and add robots to the DOM
// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', async function () {
    // Get the parent div and add robots to the DOM
    const roboterListDiv = document.getElementById('roboter-list');
    const robot_list = await getRobotsData();
    
    // Create the Robots in the List
    robot_list.forEach(robot => {
      robot = create_robot_element(robot.id)
      roboterListDiv.appendChild(robot);
    });
    
  });

// Function to send DELETE request
async function delete_data(url) {
  await fetch(url, {
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
      const response = await fetch('http://127.0.0.1:5000/robots'); // Fetch robots data
      if (!response.ok) {
          console.error(`Failed to fetch robots data: ${response.status} ${response.statusText}`);
          return []; // Return an empty array if fetch fails
      }

      const robotsData = await response.json(); // Parse the response as JSON
      console.log('Fetched robots data:', robotsData);

      // Process each robot into a standard object
      return robotsData.map(robot => ({
          id: robot.id,
          position: robot.position,
          energy: robot.energy,
          numb_packages: robot.numb_packages,
          status: robot.status,
          destination: robot.destination,
          speed: robot.speed,
          weight: robot.weight
      }));
  } catch (error) {
      console.error('Error fetching robots data:', error);
      return []; // Return an empty array on error
  }
}

async function get_config() {
  try {
      const response = await fetch('http://127.0.0.1:5000/config'); // Fetch config data
      if (!response.ok) {
          console.error(`Failed to fetch config data: ${response.status} ${response.statusText}`);
          return null; // Return null if fetch fails
      }

      const config_data = await response.json(); // Parse the response as JSON
      console.log('Fetched config data:', config_data);
      return config_data;
  } catch (error) {
      console.error('Error fetching config data:', error);
      return null; // Return null on error
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
//const url_charge_robot = `http://127.0.0.1:5000/robot/charge`;
//const url_deliever_robot = `http://127.0.0.1:5000/robots/deliever`;
//reset_sim();
//Robot_method(robotInstances[2], url_charge_robot);  // Call the method for robot with ID 1
//Robot_method(robotInstances[2], url_deliever_robot);


// Beispielausgabe in der Konsole
//console.log(robots); // Array mit Roboter-Objekten
//console.log(`Packages: ${packages}`);



