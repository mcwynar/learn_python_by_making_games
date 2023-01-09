print('      *       ')
print('     ***      ')
print('    *****     ')
print('   *******    ')
print('  *********   ')
print('      |       ')
print('      |       ')

#------------------------------------------

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5) #gives float number 2.0

print(10 ** 2)
print(7 // 2) #not rounding the result
print(7 % 2)

print((5 + 5) * 2)

print(10 > 5)
print(10 < 5)

print((1+2+3+4+5+6+7)/7)

#--------------------------------

result = 10 + 5
print(result)

result2 = result / 2
print(result2)

test = 'test'
# variable naming conventions
# 1. Use snake_case
# 2. Variable names should make sense
# 3. Variable names should be consistent

num1 = 10
num1 += 5 #num1 = num1 + 5

my_test_variable = 8
my_test_variable += 20
print(my_test_variable)

#----------------------------------

print('test')
word_length = len('another word')
print(word_length)

print(abs(-50), abs(6))
print(max(2, -7, 99, 32))

#----------------------------------

test = "A word"
print(test.upper())

username = 'john smIThXX'.title().strip('x')
print(username)

print(username.isalpha())

exercise_string = 'I like puppies'.replace('puppies', 'kittens')
print(exercise_string)

#---------------------
# Return

#---------------------------
#comments

#############
# a comment
#############

'''
This is a really important section
It does a couple of things
That we need for the code to work
'''

#----------------------------
# what you see is a physical line, it's whatever is in a single line
# Python translates this into logical lines
# a = 10; b = 20          -->     a = 10
#                                 b = 20
# c = 1 + 2 + 3 +\
# 6 + 7 + 8                 --> c = 1 + 2 + 3 + 6 + 7 + 8
print(1+2+3+\
      4+5+6)


#---------------------------
# List and tuples
# The difference between the two is that tuples are immutable, they cannot be changed
my_list = [1, 2, 3, 4.5, 'word']
print(my_list)
# my_list.clear()
my_list.reverse()
my_list.append(10)
print(my_list)

#tuple
my_tuple = (1,2,3, 1.45, 'Word', [7,8,9])
print(my_tuple)
# my_tuple.append(10) Error
# my_tuple.reverse() Error

#How to pick elements from list
# Python assigns each value in a list or tuple an index (python starts counting from 0)
# Once you have an index, you can select that element by adding [] after list or tuple
# This process is called indexing
# It works on lists, tuples & strings
# It does not work on dictionaries and sets
print("")
print(my_list[2])
print(my_tuple[5][1])
print(my_tuple[-1])

exercise_list = ['first entry', [123, 456, [0, 'Hello :)']], 'bye']
print(exercise_list[1][2][1])

# How to pick multiple elements from a list? slicing
# You still need [square brackets], like with indexing
# But now you add 2 numbers separated by a colon
# The first is the start, the second the end
# However, python only goes UP TO the end,
# it does NOT include IT

test_list = [1,2,3,4,5,6,7,8,9,10]
# [start : stop : step]
print(test_list[::-1])

# Slicing can also include a third number for the direction
# By default it is always 1, meaning we increase the index by

print(test_list[-3:0:-2])

# Unpacking
# Both list and tuples can be unpacked
# a, b = (10,5)
# a, b = [10,5]

a, b = (10,5)
print(a)
print(b)

c, d = [20, 'Hello']
print(c)
print(d)

# When creating tuples, you don't actually need brackets
# a_list = (1, 2, 3)
# a_list = 1, 2, 3

a_list = 1, 2, 3
print(a_list)

health, energy, weapon = 100, 50, 'Sword'
print(weapon)


# String, tuples and lists
test_string = 'this is a test'
test_list = [1, 2, 3, 4]

# turning a sting into a list / tuple
print(test_string.split())
print(test_string.split('t'))

print(list(test_string))
print(tuple(test_string))

#turn a list / tuple into a string
print('*'.join(['one', 'two', 'three', 'four']))
# print('*'.join(test_list))
print(str(test_list))

# indexing on strings
print(test_string[0])
print(test_string[0:5])

# exercise
print(str(test_list).strip('[]').replace(',', '').replace(' ', ''))

# dictionaries
# Complex containers for other variables
# {`key`:`value`, 1: [1, 2, 3]}
# Dictionaries store data but things are more ogranised since each value has a key

#basics
test_dict = {'A': 123, 'B': [1, 2, 3], 1: True}
print(test_dict)
# You cannot duplicate value (first will be delete)
print(test_dict.values())
print(type(test_dict.values()))
print(test_dict.keys())
print(test_dict.items())
print(len(test_dict))

#converting a dict
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))

#Getting values from dictionaries
#Indexing does not work

#Indexing with dict
print(test_dict['A'])   #does crash when it  doesn't find a key
print(test_dict.get('A'))  #doesn't crash when it cannot find a key

#Exercise
test_dict.update({'C': [3, 2, 1]})
test_dict.update(D = 'test', E = '123')
test_dict['F'] = 100
print(test_dict)

print(''*3)

# sets
# Simple containers for other variables
# {1, 'test', True}
# It has curly brackets like a dictionary but no keys
# The special thing about sets is that each value must be unique & duplicates are deleted

my_set = {1,2,3,4,4} #duplicate values will be exterminated
print(len(my_set))
#use methods
my_set.add(5)
my_set.remove(3)
print(my_set)

# indexing and slicing does NOT work
#print(my_set[0])

#print(my_set.pop())
#exercise
# use type conversion to get one item from the set by index
print(list(my_set)[2])

#Sets are very good when it comes to comparisons
# There are lots of ways to check if 2 sets have values in common (or if they differ)
#
# set1.union(set2)
# New set with shared elements

# set1.intersection(set2)
# New set with elements present in both sets

print('')
print('')
#comparison operators
set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

#suma
print(set1.union(set2))
print(set1 | set2)

#czesc wspolna
print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)

#exercise
#check if the list below has duplicate values
test_list = [43,25,324,234,5,2,32423,542,534,324,23,54,65,323,42,4,123,123,5,1,321,3124,123,123,124,1,31,23,145,3542,43,3,21,312]
print(len(test_list) == len(set(test_list)))


# Booleans can be created in lots of ways
# Integers & floats create them via comparison operators
# Strings have methods that return booleans (isnum())
# You can check if values are in lists, tuples, set or dict
# Comparing sets creates booleans
# You can also create booleans by themselves

print('')
print('')
print(1==10)
print(1!=10)

# booleans and lists and strings
print(1 in [1,2,3])
print(1 in (1,2,3))
print('e' in 'hello')
print(4 not in [1,2,3])

# booleans by themselves
print(True)
print(False)
print(not True)

e_dict = {1:'one', 2:'two', 3:'three'}
print(1 in e_dict.keys())
print('four' in e_dict.values())

# bool function
# Truthy - values that are converted to True
# Falsy - values that are converted to False
# The following values are falsy:
# 0 or 0.0 (int or float)
# '' (empty string)
# [],(),{} (empty list, tuple, set, dict)
# None (absence of a value)

# Anything else is truthy
print(bool(12))
print(bool(-1))

# There are lots of datatypes you don't explicitly use
# None - absence of a value
# sequence - to get a range of numbers
# bytes, complex numbers, memoryview, frozensets - more specific types of data you will see for highly specific purposes

print("\n"*5)

# Simple if statements
x = 15
if x > 10:
      print('the if statement was true')
      print('another line')
      y = 10
      print(y)
elif x != 0:
      print('the elif statement was correct')
else:
      print('the code that was run if the statement was false')

if 1 in [1,2,3]:
      print('another if statement')
print('some other code')

#exercise
money_available = 100
# if money  is greater or equal than 80 -> eat something fancy
# if money is greater than 45 -> eat something nice
# if money greater than 15 -> eat something okay
# else -> eat sometinhg cheap

if money_available >= 80:
      print('eat something fancy')
elif money_available > 45:
      print('eat something nice')
elif money_available > 15:
      print('eat something okay')
else:
      print('eat sometinhg cheap')


# Complex if statements

# If statements can be extended in 2 ways
# 1. You can combine conditions
# 2. You can nest them inside of each other

# combining conditions
# and + or
# if 5<1 and 'e' in 'hello' or 10!=4

# For a condition to be true as a whole
# AND
# All and parts have to be true
# This has to be true and this has to be true...

# OR
# Only 1 or parts has to be true
# This has to be true or this has to be true...

if True or False:
      print('True')






# Match case
# Match case is somewhat similar to if
# You run code if a condition is True
# Match case is better to check for one value of a long list

mood = 'hungry'

match mood:
      case 'hungry':
            print('get some food')
      case 'thirsty':
            print('get some water')
      case 'tired':
            print('get some sleep')
      #run when not of other cases are correct
      case _:
            print('any other mood')


# break    - Ends the entire while loop
# continue      - Skips the current iteration

x = 0
while x < 10:
      x += 1
      if x == 5:
            continue

      print(x)

print("\n"*3)


basic_list = [1, 2, 3]
basic_tuple = (1, 2, 3)
basic_dict = {1:"one", 2:"two", 3:"three"}
basic_set = {1, 2, 3}
basic_string = "one two three"
basic_num = 3

# for x in basic_dict:
#       print(x)

for x in basic_dict.values():
      print(x)

for x in basic_dict.items():
      print(x)

for x in basic_string:
      print(x)

for x in range(basic_num):
      print(x)

# range(start, end, step)
print(range(basic_num))

#exercise
practice_list = [[10,40,20,50], [2,42,10], [101, 10, 4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100

for x in practice_list:
      for y in x:
            if y > 100:
                  break
            elif y >= 50 or y < 10:
                  continue
            else:
                  print(y)

print('\n' *3)

# for x in [1, 2, 3]:           OR           for x in [1, 2, 3]: print(x)
#       print(x)

# if x == 5:                    OR           if x==5: print(x)
#       print(x)

# while x<5:                    OR           while x<5: x+=1; print('stuff')
#       x+=1
#       print('stuff')




x = 5
# Ternary operator
# True value if expression else False value

# I want a color blue if the value of x  is below five, if that is not the case so else I want the color red
color = 'blue' if x<5 else 'red'
print(color)

x = 1
print(f"The color is {'red' if x < 5 else 'blue'}")

a = ['red' if x < 5 else 'blue', 'yellow', 'green']
print(a)