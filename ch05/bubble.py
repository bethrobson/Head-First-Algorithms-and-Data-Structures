
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        print(f"After pass {i+1}: {nums}")
        if not swapped:
            break

nums = [4, 2, 6, 1, 5, 3]
print(nums)
bubble_sort(nums)
print(nums)


