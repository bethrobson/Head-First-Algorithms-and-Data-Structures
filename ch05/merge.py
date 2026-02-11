
def merge_sort(nums):
    if len(nums) <= 1:
       return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    sorted_nums = merge(left_sorted, right_sorted)
    print(f"After merge: {sorted_nums}")
    return sorted_nums

def merge(left, right):
    sorted_nums = []
    left_index = 0
    right_index = 0
    while (left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            sorted_nums.append(left[left_index])
            left_index += 1
        else:
            sorted_nums.append(right[right_index])
            right_index += 1
    sorted_nums.extend(left[left_index:])
    sorted_nums.extend(right[right_index:])
    return sorted_nums

nums = [4, 2, 6, 1, 5, 3]
print(nums)
sorted_nums = merge_sort(nums)
print(sorted_nums)


