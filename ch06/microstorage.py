from datetime import datetime

class MicroStorage:
    def __init__(self):
        self.storage = {}
        self.num_boxes = 0

    def store(self, description, owner):
        now = datetime.now().strftime("%m/%d/%Y %I:%M %p")
        key = (description, owner)
        access_num = 0
        if key in self.storage:
            now, access_num = self.storage[key]
        access_num += 1
        self.storage[key] = (now, access_num)
        self.num_boxes += 1
        print(f"({description, owner}) stored at {now}, {access_num} times")

    def retrieve(self, description, owner):
        print(f"({description, owner}) item retrieved")
        return self.storage[(description, owner)]

    def print(self):
        print(f"\n---- Micro-Storage warehouse: {self.num_boxes} items ----")
        print(self.storage)

micro_storage = MicroStorage()
micro_storage.store("Air Fryer", "Marianne")
micro_storage.store("Bath Bombs", "Alex")
micro_storage.store("Bath Bombs", "Sam")
micro_storage.store("Coffee Grinder", "Elise")
micro_storage.store("Essential Oils", "Kim")
micro_storage.store("Umbrella", "Kim")

micro_storage.print()

print(f"Alex's Bath Bombs: {micro_storage.retrieve('Bath Bombs', 'Alex')}")
micro_storage.store("Bath Bombs", "Alex")

