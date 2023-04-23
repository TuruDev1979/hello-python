### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
my_list = [i for i in range(9)]

print(my_original_list)
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(9)]
print(my_list)