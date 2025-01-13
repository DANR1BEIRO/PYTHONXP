import time

class CountDownClock:     
        def __init__(self):
            self.countDown = self.selectCountDown()
            self.amountCountDown()
            
        countDown = {
            1: "seconds",
            2: "minutes",
            3: "hours",
        }
        
        def selectCountDown(self):
            while True:
                try:
                    choice = int(input("""Which countdown do you prefer?
                    \n[1] Seconds\n[2] Minutes\n[3] Hours\n"""))
                    
                    if choice in self.countDown:
                        return self.countDown[choice]
                    else: 
                        print("Select one of the three options!")
                except ValueError:
                    print("only numbers between 1 to 3 are allowed!")
                    
        def amountCountDown(self):
            while True:
                try:
                    userTime = int(input(f"Enter the time in {self.countDown}: "))
                    if userTime <= 0:
                        print("Enter a positive number!")
                        continue
                    if self.countDown == "minutes":
                        userTime *= 60
                    elif self.countDown == "hours":
                        userTime *= 3600
                    
                    for counter in range(userTime, 0, -1):
                        seconds = counter % 60
                        minutes = (counter // 60) % 60
                        hours = counter // 3600
                        print(f"{hours:2}:{minutes:02}:{seconds:02}")
                        time.sleep(1)
                        
                    print("TIME'S UP!")
                    return 
                    
                except ValueError:
                    print("Only integer numbers are allowed!")
                    
if __name__=="__main__":
    CountDownClock()

