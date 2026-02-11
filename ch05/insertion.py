
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        print(f"After inserting at index {j+1} ({key}): {nums}")

nums = [4, 2, 6, 1, 5, 3]
print(nums)
insertion_sort(nums)
print(nums)


