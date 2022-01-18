def add_indexes(nums):
    for index in range(len(nums)):
        nums[index] += index
        # nums[index] = nums[index] + index
    return nums


print(add_indexes([0, 0, 0, 0, 0]))  # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))  # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))  # ➞ [5, 5, 5, 5, 5]
