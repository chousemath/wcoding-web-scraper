def find_odd(nums):
    counts = {}  # dict()
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for key, value in counts.items():
        if value % 2 == 1:
            return key


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))  # ➞ -1
print(find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))  # ➞ 5
print(find_odd([10]))  # ➞ 10
