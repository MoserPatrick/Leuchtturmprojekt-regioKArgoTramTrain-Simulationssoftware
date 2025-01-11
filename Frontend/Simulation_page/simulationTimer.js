export class simulationTimer {
    constructor() {
      this.start_time = 12 * 60;  // Start time in minutes (12:00 = 720 minutes)
      this.currentTime = this.start_time; 
      this.endTime = 18 * 60; // End time in minutes (18:00 = 1080 minutes)
      this.timeStep = 1; // Time step in minutes per "tick"
      this.running = False
    }
  
    // Advance the simulation time
    advanceTime() {
      if(this.running){
          this.currentTime += this.timeStep;
      

        // Reset to 12:00 if we hit 18:00
        if (this.currentTime >= this.endTime) {
          this.currentTime = this.start_time;
          console.log("Timer reset to 12:00.");
        }
      }
    }
  
    stop(){
      this.running = False
    }

    start(){
      this.running = True
    }

    // Get the current simulation time in HH:MM format
    getCurrentTime() {
      const hours = Math.floor(this.currentTime / 60);
      const minutes = this.currentTime % 60;
      return `${hours.toString().padStart(2, "0")}:${minutes
        .toString()
        .padStart(2, "0")}`;
    }
  
    // Reset the timer to 12:00
    reset() {
      this.currentTime = this.start_time;
      console.log("Timer manually reset to 12:00.");
    }
  }
  
  