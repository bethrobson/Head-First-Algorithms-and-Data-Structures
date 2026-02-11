
def selection_sort(data):
    n = len(data)
    for i in range(n):
        # Assume the current position has the minimum
        min_index = i
        # Look for a smaller element in the rest of the dataay
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        # Swap if we found a smaller element
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]

numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers)

