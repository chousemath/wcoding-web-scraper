def missing_num(nums):
    values = [n for n in range(1, 11)]
    for num in nums:  # [1, 2, 3, 4, 6, 7, 8, 9, 10]
        # values = [0, 0, 0, 0, 5, 0, 0, 0, 0, 0]
        values[num - 1] = 0
    for value in values:
        if value != 0:
            return value
    return 0


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # ➞ 5
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))  # ➞ 10
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))  # ➞ 7
