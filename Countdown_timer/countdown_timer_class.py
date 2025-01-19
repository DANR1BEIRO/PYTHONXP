import time

class countdowntimer:
    """
    A class to create a countdown timer based on user 
    selected units of time (seconds, minutes, hours).
    """
    def __init__(self):
        self.time_measurement = self.get_time()
        self.time_amout()

    time_dict = {
        1: "seconds",
        2: "minutes",
        3: "hours"
    }
    
    def get_time(self): 
        """
        Prompt the user to select a unit of time for the countdown.
        
        returns:
        str: The selected unit of time as a string ('seconds', 'minutes', 'hours').;
        """
        while True:
            try:
                choose = int(input("Choose which unit of time you prefer:\n[1] Seconds\n[2] Minutes\n[3] Hours\n"))
                if choose in self.time_dict:
                    return self.time_dict[choose]
                else:
                    print("Select one of the 3 options available")
            except ValueError:
                print("Only integer numbers between 1 and 3 are allowed")

    def time_amout(self):
        """
        Prompts the user to enter the countdown duration in the selected unit of time.
        Converts the duration into seconds if necessary and performs the countdown.
        
        The countdown is displayed in HH:MM:SS format and updates every second
        
        returns:
        Prints the countdown and the message "TIME'S UP!" at the end.
        """
        while True:
            try:
                choose = int(input(f"Enter how much {self.time_measurement} do you want: "))
                if choose > 0:
                    if self.time_measurement == 'minutes':
                        choose *= 60
                    if self.time_measurement == 'hours':
                        choose *= 3600
                                        
                    for counter in range(choose, 0, -1):
                        seconds = counter % 60
                        minutes = (counter // 60) % 60
                        hours = counter // 3600
                        print(f"{hours:02}:{minutes:02}:{seconds:02}")
                        time.sleep(1)
                        
                    print("TIME'S UP!")
                    break
                
                else:
                    print("time must be greater than zero")
            except ValueError:
                print("Only integer numbers are allowed")
        
if __name__=="__main__":
    countdowntimer()
   
