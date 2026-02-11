from queue import Queue 

class Taxi:
    def __init__(self, taxi_id):
        global line
        self.rider = None
        self.taxi_id = taxi_id

    def arrives(self):
        if line:
            self.rider = line.pop()
            print(f"Taxi {self.taxi_id} takes {self.rider}")
        else:
            print(f"Taxi {self.taxi_id} waits for a passenger")

    def __str__(self):
        return f"Taxi {self.taxi_id} is carrying {self.rider}"

line = Queue(["Ava", "Ben", "Cara", "Diego", "Eden"])

print(f"Initial line waiting for a taxi: {line}")

taxi_101 = Taxi("TX-101")
taxi_102 = Taxi("TX_102")
taxi_103 = Taxi("TX_103")
taxi_104 = Taxi("TX_104")

# a couple of taxis pull up
taxi_101.arrives()
taxi_102.arrives()

# more passengers arrive
print("Finn joins the line")
line.push("Finn")
print("Gio joins the line")
line.push("Gio")

# more taxis arrive
taxi_103.arrives()
taxi_104.arrives()

print(f"Still in line: {line}")

