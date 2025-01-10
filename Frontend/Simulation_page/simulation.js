
const url_get_robots = `http://127.0.0.1:5000/robots`;

async function getRobotsData() {
    try {
        const response = await fetch(url_get_robots);  // Fetch robots data from Flask server
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

const url_charge_robot = `http://127.0.0.1:5000/robot/charge`
async function chargeRobot(robot) {
    try {
        const response = await fetch(url_charge_robot, {
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
chargeRobot(1);  // Call the method for robot with ID 1



// Example usage to fetch and store robot data in an array
getRobotsData();

/*
fetch(url_get_robots)
    .then(response => {
        if (!response.ok) {
            console.error(`Error: Received status code ${response.status}`);
            return null;
        }
        return response.json();
    })
    .then(data => {
        console.log('Fetched Robots:', data);

        // Convert each robot dictionary into a Robot object
        const robots = data.map(robotData => Robot.fromDict(robotData));

        // Now you can use the Robot objects
        robots.forEach(robot => {
            console.log(`Robot ID: ${robot.id}, Position: ${robot.position}`);
        });
    })
    .catch(error => {
        console.error("Error fetching robot data:", error);
    });*/

// Beispielausgabe in der Konsole
//console.log(robots); // Array mit Roboter-Objekten
//console.log(`Packages: ${packages}`);



