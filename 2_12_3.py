class TVController():

    def __init__(self, channels):
        self.channels = channels
        self.current_channel = self.channels[0]
        print(self.current_channel)

    def add_channels(self, name):
        self.channels.append(name)

    def delete_channels(self, name):
        self.channels.remove(name)

    def first_channel(self):
        self.current_channel = self.channels[0]
        print(self.current_channel)

    def last_channel(self):
        self.current_channel = self.channels[-1]
        print(self.current_channel)

    def turn_channel(self, n):
        self.current_channel = self.channels[n-1]
        print(self.current_channel)

    def next_channel(self):
        ind = self.channels.index(self.current_channel)
        if ind == len(self.channels) - 1:
            self.current_channel = self.channels[0]
            print(self.current_channel)
        else:
            self.current_channel = self.channels[ind+1]
            print(self.current_channel)

    def previous_channel(self):
        ind = self.channels.index(self.current_channel)
        if ind == 0:
            self.current_channel = self.channels[-1]
            print(self.current_channel)
        else:
            self.current_channel = self.channels[ind-1]
            print(self.current_channel)

    def current(self):
        print(self.current_channel)

    def is_exist(self, name):
        if name is self.channels or int(name)-1 <= len(self.channels):
            print("Yes")
        else:
            print("No")


massage_1 = "add channel: A, first channel: F, last channel: L, turn channel: T\nnext: N, previous: P, "\
            "delete channel: D, current channel: C\nis exist: I, exit: E"
massage_2 = "Name channel: "
massage_3 = "Number channel: "
massage_4 = "Number or Name channel: "


def commands(tv_cont):
    command = input("command: ")
    if command.lower() == "a":
        channels = input(massage_2)
        tv_cont.add_channels(channels)
    elif command.lower() == "f":
        tv_cont.first_channel()
    elif command.lower() == "l":
        tv_cont.last_channel()
    elif command.lower() == "t":
        number = input(massage_3)
        tv_cont.turn_channel(number)
    elif command.lower() == "n":
        tv_cont.next_channel()
    elif command.lower() == "p":
        tv_cont.previous_channel()
    elif command.lower() == "d":
        channels = input(massage_2)
        tv_cont.delete_channels(name=channels)
    elif command.lower() == "c":
        tv_cont.current()
    elif command.lower() == "i":
        channels = input(massage_4)
        tv_cont.is_exist(channels)
    elif command.lower() == "e":
        exit(0)


list_channels = ["BBC", "Discovery", "TV1000"]
tv_controller = TVController(list_channels)
print(massage_1)
while True:
    commands(tv_controller)
