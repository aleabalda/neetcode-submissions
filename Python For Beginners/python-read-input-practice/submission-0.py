def add_two_numbers() -> int:
    user_input = input()
    nums = user_input.split(",")
    sum_nums = 0
    for num in nums:
        sum_nums += int(num)
    return sum_nums



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
