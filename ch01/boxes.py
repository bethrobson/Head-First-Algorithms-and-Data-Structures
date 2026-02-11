boxes = ["Air Fryer", "Bath Bombs", "Bluetooth Speaker", "Coffee Grinder", "Desk Organizer", "Essential Oils", "Face Mask", "Guitar Stand", "Hair Dryer", "Ice Maker", "Jade Roller", "Keyboard", "Laptop Sleeve", "Luna Lamp", "Microwave", "Neon Sign", "Notebook", "Office Chair", "Phone Dock", "Plant Pot", "Rice Cooker", "Smart Bulb", "Tablet Stand", "Umbrella", "Vacuum", "Wall Hooks", "Wireless Charger", "Yoga Mat", "Zipper Pouch"]

def linear_search(boxes, target_item):
    for i in range(len(boxes)):
        if boxes[i] == target_item:
            return i
        else:  
            print(f"Not in box {i}")
    return -1

print("Linear Search")
box = linear_search(boxes, "Rice Cooker")

if box != -1:
    print(f"Found at box {box}")
else:
    print("Item not found")


def binary_search(boxes, target_item):
    left = 0
    right = len(boxes) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = boxes[mid]

        if guess == target_item:
            return mid 
        elif guess < target_item:
            left = mid + 1
        else:
            right = mid - 1
            
        print(f"Not in box {mid}")

    return -1

print("Binary Search")
box = binary_search(boxes, "Rice Cooker")

if box != -1:
    print(f"Found at box {box}")
else:
    print("Item not found")


