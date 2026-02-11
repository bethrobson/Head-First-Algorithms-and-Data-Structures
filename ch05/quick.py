# numbers with quicksort

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        print(f"Sort {nums} with pivot {pivot}")
        smaller, larger = [], []
        for n in nums[1:]:
            if n <= pivot: 
               smaller.append(n)
            if n > pivot: 
               larger.append(n)
        return quicksort(smaller) + [pivot] + quicksort(larger)


nums = [4, 2, 6, 1, 5, 3, 8, 7]
nums2 = [1, 8, 2, 7, 3, 5, 4, 6]

print(f"Original: {nums}")
sorted_nums = quicksort(nums)
print(f"Sorted result: {sorted_nums}")

print(f"Original: {nums2}")
sorted_nums = quicksort(nums2)
print(f"Sorted result: {sorted_nums}")


def quicksort_in_place(nums, low=0, high=None):
    if high is None:
        high = len(nums)-1

    if low < high:
        pivot = nums[high]
        print(f"Sort {nums} with pivot {pivot}")
        start = low - 1
        for end in range(low, high):
            if nums[end] < pivot:
                start += 1
                if start != end:
                    nums[start], nums[end] = nums[end], nums[start] 
        pivotIndex = start + 1
        nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]
        quicksort_in_place(nums, low, pivotIndex - 1)
        quicksort_in_place(nums, pivotIndex + 1, high)

#print(f"Original: {nums}")
#quicksort_in_place(nums)
#print(f"Sorted result (in place): {nums}")


