class TV:
    def __init__(self, channelmin, channelmax):
        self.on = False
        self.channel = 2
        self.channelmin = channelmin
        self.channelmax = channelmax
        
    def decreaseChannel(self):
        if self.channel -1 >= self.channelmin:
            self.channel -= 1
    def increaseChannel(self):
        if self.channel + 1 <= self.channelmax:
            self.channel += 1
            
tv = TV(1, 99)
for x in range(0, 120):
    tv.increaseChannel()
print(tv.channel)

for x in range(0, 120):
    tv.decreaseChannel()
print(tv.channel)