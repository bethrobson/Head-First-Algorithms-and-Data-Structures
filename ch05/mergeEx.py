
def merge_sort(array):
    if len(array) <= 1:
       return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    sorted_array = merge(left_sorted, right_sorted)
    print(f"After merge: {sorted_array}")
    return sorted_array

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0
    while (left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array

names = ["Ravi", "Chris", "Anna", "John", "Luke", "Zoe"]
print(names)
sorted_array = merge_sort(names)
print(sorted_array)


