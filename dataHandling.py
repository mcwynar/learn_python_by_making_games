# -----------------------------
#           Lesson 1
# -----------------------------
# Manipulating lists & for loops


# Often you want to merge lists and loop over the result
# We can zip lists together and we can give each list and index inside of the loop



inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]

# print(list(zip(inventory_names, inventory_numbers)))

# for thing in zip(inventory_names, inventory_numbers):
#     print(thing)

# for name, number in zip(inventory_names, inventory_numbers):
#     print(f"{name} current inventory: {number}")



# enumerate function - get the current index
# print(list(enumerate(inventory_names)))

for index, name in enumerate(inventory_names):
    print(f"{index}: {name}")
    if index == len(inventory_names) // 2:
        print("halway done!")



# Exercise
#combine zip and enumerate to get 'Screws [id:0] - inventory: 43'

for index, inventory in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{inventory[0]} [id:{index}] - inventory: {inventory[1]}")





print('\n'*3)
# -----------------------------
#           Lesson 2
# -----------------------------
# List comprehension



# List comprehension is a way to create lists on one line of code
# It is one of the most powerful features in python
# You can use it to create simple lists and you can use it to manipulate existing lists


# You want to create a list with the numbers from 0 to 99
# my_list = []
# for num in range(0,100):
#     my_list.append(num)

# or

my_list = [num for num in range(0, 100)]
print(my_list, "\n"*2)



# You can combine list comprehension with a ternary operator
my_list_2 = [num for num in range(0,100) if num <10]
print(my_list_2)

# or

my_list_3 = [num if num < 10 else 0 for num in range(0, 100)]
print(my_list_3, "\n"*2)


inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]
replenish_list = [thing for thing in zip(inventory_names, inventory_numbers) if thing[1]<25]
print(replenish_list, "\n"*2)



# combine list comprehension
# comined_comp = [[x for x in range(5)] for y in range(10)]
# for row in comined_comp:
#     print(row)


comined_comp = [[(x,y) for x in range(5)] for y in range(10)]
for row in comined_comp:
    print(row, "\n"*2)
# print(comined_comp)


# Exercise
# create the fields for a chess board
#abcdefgh
#12345678
# chess_board = [[(chr(x), y) for x in range(65, 73)] for y in range(1,9)]
# # print(chr(65)) #A
# # print(chess_board)
# for row in chess_board:
#     print(row)



chess_board = [[(chr(x), y) for x in range(65, 73)] for y in range(8,0, -1)]
# print(chr(65)) #A
# print(chess_board)
for row in chess_board:
    print(row)

print('\n'*2)
#or

chess_board2 = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board2:
    print(row)


print('\n'*3)
# -----------------------------
#           Lesson 3
# -----------------------------
# Other comprehension


# Besides list comprehension, you can also create dict and set comprehension

# we always need the key then a colon and then a value
# dict_comp = (num: num for num in range(10))

# set)comp = {num for num in range(10)}

#tuple_comp = tuple(num for num in range(10))

# 1. set comprehension
set_comp = {num for num in range(100)}
print(set_comp, '\n'*3)


# 2. dictionary comprehension
dict_comp = {num: num**2 for num in range(20)}
print(dict_comp, '\n'*3)


# 3. tuple comprehension
tuple_comp = tuple(num for num in range(20))
print(tuple_comp, '\n'*3)


# Exercise
# create a dictionary with the keys 'A', 'B', 'C', 'D' and 'E'
# each key should have a list as value with the values [1, 2, 3, 4, 5]

exercise_comp = {key: [1, 2, 3, 4, 5] for key in "ABCDE"}
print(exercise_comp)


print('\n'*3)
# -----------------------------
#           Lesson 4
# -----------------------------
# Functions that take functions as arguments

list1 = [4, 2, 3, 1, 5]
# print(sorted(list1, reverse= True))
print(sorted(list1, reverse=True,))

list2 = [('a', 3), ('b', 10), ('c', 6), ('d', 5)]

def sort_function(item):
    #return int from tuple
    return item[1]
# We are only passing in the function, not calling the function
print(sorted(list2, key = sort_function))
print(sorted(list2, key = lambda item: item[1]))
print('\n'*2)

# Exercise
inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
inventory_numbers = [43, 12, 95, 421, 23, 43]
comined_list = list(zip(inventory_names, inventory_numbers))
print(comined_list)
# 1. sort this list by inventory numbers
# 2. sort this list by length of the inventory name

# 1
print(sorted(comined_list, key = lambda inv_tuple: inv_tuple[1]))
# 2
print(sorted(comined_list, key = lambda inv_tuple: len(inv_tuple[0])))



print('\n'*3)
# -----------------------------
#           Lesson 5
# -----------------------------
# Map & Filter
my_list = [1, 2, 3, 4, 5]


# map - changes values with a function inside of a iterable
# map(key, iterable)

# def power_function(number):
#     return number**2
# print(list(map(power_function, my_list)))
print(list(map(lambda number: number**2, my_list)))

# filter - filters out values from a condition
# filter(key, iterable)

def get_below_4(number):
    if number<4:
        return True
    else:
        False
print(list(filter(get_below_4, my_list)))
print(list(filter(lambda number: True if number<4 else False, my_list)))
print(list(filter(lambda number: number<4, my_list)))

# Exercise
# convert the power function and the filter one to list comprehension
power_comp_list = [number**2 for number in my_list]
below_4_comp_list = [number for number in my_list if number<4]
print(power_comp_list, below_4_comp_list)



print('\n'*3)
# -----------------------------
#           Lesson 6
# -----------------------------
# File handling


# open and close it manually
# file = open('test.txt')
# print(list(file))
# file.close()



# open and close it automatically
with open('test.txt') as file:
    # print(type(file.read()))
    # print(file.read())
    for line in list(file):
        print(line)


# write some file
# r - read; a - append; w - write
# default is r
# with open('test.txt', 'a') as file:
#     file.write("\nXXXXXXXXXXXXXXXWrite some more textXXXXXXXXXX")

# "w" create new file if can't found file with this name otherwise overwrite whole file
with open("new_file.txt", "w") as file:
    file.write("Test message\n")

# Exercise
# create a new text file and draw a tree in it
with open("new_file.txt", "w") as file:
    file.write("""    *
   ***
  *****
 *******
*********
    |
    |
    """)



print('\n'*3)
# -----------------------------
#           Lesson 7
# -----------------------------
# Deleting data

# Python can delete things with del thing
# This would remove variables but you rarely use it that way
# In most cases, you only delete values inside of lists

# a = 1
# del a
# print(a)

# remove items from a list
a = [1, 2, 3, 4, 5]

#del (removes item by index)
del a[1]
print(a)
print(a[1])

# remove an item by value
a.remove(5)
print(a)

# pop (default values is -1 - last item)
print(a.pop(-1))
print(a)

#clear the entire list
a.clear()
print(a)