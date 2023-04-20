###### Listas ######

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[my_list.count(30)])


my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "azul")
print(my_other_list)

my_other_list[1] = 'Rojo'
print(my_other_list)

del my_list[2]
print(my_list)

my_list.remove(30)
print(my_list)

my_list.clear()
print(my_list)

my_other_list.reverse()
print(my_other_list)