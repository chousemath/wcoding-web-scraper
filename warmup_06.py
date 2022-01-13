def move_to_end(values, target):
    new_values = []
    count = 0
    for value in values:
        if value != target:
            new_values.append(value)
        else:
            count += 1

    # [3, 2, 4, 4] /////// count = 2
    # [3, 2, 4, 4] + [1] * 2
    # [3, 2, 4, 4] + [1, 1]
    # [3, 2, 4, 4, 1, 1]
    return new_values + [target] * count


print(move_to_end([1, 3, 2, 4, 4, 1], 1))  # ➞ [3, 2, 4, 4, 1, 1]
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))  # ➞ [7, 8, 1, 2, 3, 4, 9]
print(move_to_end(["a", "a", "a", "b"], "a"))  # ➞ ["b", "a", "a", "a"]
