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


async function create_top_line(config){
      // Create the left section (d-flex)
  
  const leftDiv = document.createElement('div');
  leftDiv.classList.add('left', 'd-flex');

  // Create the p elements inside the left div
  const leftP1 = document.createElement('p');
  leftP1.textContent = 'Number Of Robots:   ' + JSON.stringify(config.numb_robots);
  const leftP2 = document.createElement('p');
  leftP2.textContent = 'Number Of Packages:   ' + JSON.stringify(config.max_packages);

  // Append the p elements to the left div
  leftDiv.appendChild(leftP1);
  leftDiv.appendChild(leftP2);

  // Create the right section (d-flex)
  const rightDiv = document.createElement('div');
  rightDiv.classList.add('right', 'd-flex');

  // Create the p element for speed inside the right div
  const rightP = document.createElement('p');
  rightP.textContent = 'Speed:   ' + JSON.stringify(config.sim_speed);

  // Create the cancel simulation button
  const cancelButton = document.createElement('button');
  cancelButton.classList.add('cancel-simulation');
  cancelButton.id = 'cancel-simulation';
  cancelButton.textContent = 'Cancel Simulation';

  // Add event listener for the button
  cancelButton.addEventListener('click', () => cancel_button()); 

  // Append the p and button elements to the right div
  rightDiv.appendChild(rightP);
  rightDiv.appendChild(cancelButton);

  // Now append both left and right divs to a parent container, for example:
  const top_line = document.getElementById('top-line'); // Assuming you have a container with this id
  top_line.appendChild(leftDiv);
  top_line.appendChild(rightDiv);

}


async function show_robot(robot){
    console.log(`Button for robot ${robot.id} clicked`);
    console.log("type"+ typeof(robot));
    // creating elements to showcase the robots data
    // remove past containers
    const existing_info_icons = document.querySelector('.info-icons');
    // If it exists, remove it
    if (existing_info_icons) {
        existing_info_icons.remove();
    }
    const existinglocDest = document.querySelector('.location-destination');
    // If it exists, remove it
    if (existinglocDest) {
        existinglocDest.remove();
    }
    // create big container called "info-icons"
    const iconContainer = document.createElement('div');
    iconContainer.classList.add('info-icons');
    iconContainer.id = `icon-${robot.id}`;

    // Define the icon data (image sources and the text)
    const icons = [
      { src: 'images/Robot.png', text: robot.id, id: `robot-id-${robot.id}` },
      { src: 'images/box.png', text: robot.numb_packages, id: `packages-${robot.id}` },
      { src: 'images/bigbattery.png', text: robot.energy, id: `energy-${robot.id}` },
      { src: 'images/Delivering.png', text: robot.status, id: `status-${robot.id}` },
      { src: 'images/Speed.png', text: robot.speed, id: `speed-${robot.id}` },
      { src: 'images/Weight.png', text: robot.weight, id: `weight-${robot.id}` }
    ];

    // Loop through the icon data to create list items dynamically
    icons.forEach(icon => {
        const single_icon = document.createElement('li');
        single_icon.classList.add('single-icon');

        const image = document.createElement('img');
        image.src = icon.src;

        const paragraph = document.createElement('p');
        paragraph.textContent = icon.text;

        // Append the image and paragraph to the list item
        single_icon.appendChild(image);
        single_icon.appendChild(paragraph);

        // Append the list item to the container
        iconContainer.appendChild(single_icon);
    });

    // Location Info side
    const locationDestination = document.createElement('div');
    locationDestination.classList.add('location-destination');
    locationDestination.id = `locdest-${robot.id}`;

    // Select station in drop down menu
    /*
    // Create the select element
    const dropdown = document.createElement("select");
    dropdown.id = "objectDropdown"; // Set an ID
    dropdown.classList.add('location');

    // Sample objects
    const stations = [
      { trias_id: 1, name: "Object A", pos: [1,1] },
      { trias_id: 2, name: "Object B" , pos: [1,1]},
      { trias_id: 3, name: "Object C" , pos: [3,3]}
  ];

    // Populate the dropdown
    stations.forEach(obj => {
        const option = document.createElement("option");
        option.value = JSON.stringify(obj.pos)//obj.trias_id; // Store object ID as value
        option.textContent = obj.name; // Show object name
        dropdown.appendChild(option);
    });

    
      dropdown.addEventListener("change", async () => {
        // Convert dropdown value to array or number (assuming "1,1" format)
        robot.start_pos = JSON.parse(dropdown.value );
        console.log(robot.package_list);
        const json_robot = robot_toJSON(robot);

        patchRobot(robot.id, json_robot);

    });
    */
    
    // Create the location div
    const location = document.createElement('div');
    location.classList.add('location');

    // Create the image for the location
    const locationImage = document.createElement('img');
    locationImage.src = 'images/pngegg.png'; // Set image source
    location.appendChild(locationImage);

    // Create the paragraph for the location text
    const locationText = document.createElement('p');
    locationText.id = `location-${robot.id}`;
    const start_pos = JSON.parse(robot.start_pos)
    locationText.textContent = JSON.stringify(start_pos.name); // Set location text
    location.appendChild(locationText);

    // Create the destination div
    const destination = document.createElement('div');
    destination.classList.add('destination');

    // Create the paragraph for the destination text
    const destinationText = document.createElement('p');
    const dest = JSON.parse(robot.dest)
    destinationText.textContent = JSON.stringify(dest.name); // Set destination text
    destinationText.id = `destination-text-${robot.id}`;
    destination.appendChild(destinationText);

    // Create the image for the destination
    const destinationImage = document.createElement('img');
    destinationImage.src = 'images/pngegg.png'; // Set image source
    destination.appendChild(destinationImage);

    // Append the location and destination divs to the main container
    //locationDestination.appendChild(dropdown);
    locationDestination.appendChild(location);
    locationDestination.appendChild(destination);

    // Append the icon container other parent element called "info-sheet"
    const info_sheet = document.getElementById('info-sheet');
    const test = document.createElement('button');
    test.classList.add('destination');

    test.addEventListener('click', () => test_button(robot));
    //info_sheet.appendChild(test)
    info_sheet.appendChild(iconContainer);  // Or any other container
    info_sheet.appendChild(locationDestination)



}


function update_robot(robot_id, updated_fields) {
  console.log(`Updating robot ${robot_id} with attributes`, updated_fields);
  const existing_info_icons = document.querySelector('.info-icons');
    // If it exists, remove it
    if (existing_info_icons) {
       if(existing_info_icons.id != `icon-${robot.id}`){
          return
       }   
    }
    const existinglocDest = document.querySelector('.location-destination');
    // If it exists, remove it
    if (existinglocDest) {
      if(existinglocDest.id != `locdest-${robot.id}`){
        return
     }   
    }
    for (const [key, value] of Object.entries(updated_fields)) {
      const elementId = `${key}-${robot_id}`;
      const element = document.getElementById(elementId);

      if (element) {
          if (element.tagName === 'P') {
              element.textContent = value; // Update text content for paragraphs
          } else {
              console.warn(`Unhandled element type for ${elementId}`);
          }
      } else {
          console.warn(`Element with ID ${elementId} not found.`);
      }
  }
}

// Establish a WebSocket connection to the backend
const socket = io('http://127.0.0.1:5000');

socket.on("connect", () => {
  console.log("Connected to Flask-SocketIO server!");
});

// Listen for updates from the server
socket.on('robot_updated', (robot_id, updated_attributes) => {


  update_robot(robot_id, updated_attributes);
});


// creating the right Robot list
function create_robot_element(robot) {
  const image_robot = './images/Robot.png'; 

  // Create a button element instead of an <li>
  const button_robot = document.createElement('button');
  button_robot.classList.add('single-roboter'); // Add your styling class
  button_robot.id = `robot-${robot.id}`; // Set the id for the button
  button_robot.innerHTML = `${robot.id}. <img src="${image_robot}" alt="Robot" />`; // Add the image and ID text

  // (Optional) Add event listener
  button_robot.addEventListener('click', () => show_robot(robot));

  return button_robot
  }
  
async function test_button(robot){
  console.log("clicked test");
  const url_test = 'http://127.0.0.1:5000/robot/charge';
  await Robot_method(robot, url_test);
}

async function cancel_button(){
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
}


  // Get the parent div and add robots to the DOM
// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', async function () {

    const config_top_line = await get_config();
    create_top_line(config_top_line);

    // Get the parent div and add robots to the DOM
    const roboterListDiv = document.getElementById('roboter-list');
    const robot_list = await getRobotsData();
    
    // Create the Robots in the List
    robot_list.forEach(robot => {
      const robot_element = create_robot_element(robot)
      roboterListDiv.appendChild(robot_element);
      
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
          package_list: robot.package_list,
          status: robot.status,
          dest: robot.dest,
          speed: robot.speed,
          weight: robot.weight,
          start_pos: robot.start_pos
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



