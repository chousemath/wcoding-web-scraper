def factorial(num):
    total = 1
    while num > 0:
        # total *= num
        total = total * num
        num -= 1
    return total

# total: 1 => 3 => 6 => 6
#   num: 3 => 2 => 1 => 0

#val = 55
#name = 'Joseph'
#
#def factorial(num):
#    if num == 1:
#        return 1
#    return num * factorial(num - 1)

# 3 * 2 * 1
print(factorial(3)) # ➞ 6
print(factorial(5))# ➞ 120
print(factorial(13)) # ➞ 6227020800
