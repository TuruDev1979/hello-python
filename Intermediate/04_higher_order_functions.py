### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Clousures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(5))

numbers = [2, 5, 10, 21, 3, 30]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_that_ten(number):
    if number > 10:
        return True
    else:
        return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value + third_value

reduce(sum_two_values,numbers)