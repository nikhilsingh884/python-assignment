# question:2 how will you remove last object from a list?.
# suppose list1 is [2,33,555,34,adn 35],what is list[-1]?

import math
from collections import Counter
import random
list1 = [2, 33, 555, 34, 35]
list1.pop()

# what is list[-1]?

list1 = [2, 33, 555, 34, 35]
list1[-1]

# Question 4: Write a Python function to get the largest number, smallest num and sum of all from a list.

lst = [10, 5, 15, 7, 50, 100, 1]
print(max(lst))
print(min(lst))
print(sum(lst))


# Question 6: Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

def match_words(words):
    ctr = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
        return ctr


print(match_words(['abc', 'xyz', 'aba', '1221']))


# Question 7 : Write a Python program to remove duplicates from a list.

list1 = [11, 5, 3, 133, 3, 2, 2, 2, 3, 3,
         3, 4, 4, 4, 4, 454, 100, 666, 1, 1, 12]
a = set(list1)
b = list(a)
print(b)


# Question 8 : Write a Python program to check a list is empty or not.

list1 = [1, 5, 4, 3.5, 'tiger', True]
if len(list1) == 0:
    print('The List is empty')
else:
    print('The List is not empty')

    # Question 9 : Write a Python function that takes two lists and returns true if they have at least one common member.


def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [6, 2, 8, 9, 10]
result1 = has_common_member(list1, list2)

print(result1)


# Question 10 : Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30

my_list = [i**2 for i in range(1, 31)]

# Print the first 5 elements
print("First 5 elements:")
print(my_list[:5])

# Print the last 5 elements
print("Last 5 elements:")
print(my_list[-5:])


# Question 10: Write a Python function that takes a list and returns a new list with unique elements of the first list.

lst = [11, 5, 3, 133, 3, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 454, 100, 666, 1, 1, 12]
a = set(lst)
my_set = a
my_list = list(my_set)
print(my_list)


# Question 12: Write a Python program to convert a list of characters into a string.

# Define a list of characters
char_list = ['H', 'e', 'l', 'l', 'o', 'h', 'i']
string = ''.join(char_list)
print(string)


# Question 13: Write a Python program to select an item randomly from a list.

items = ['apple', 'banana', 'orange', 'pear', 'grape']
random_item = random.choice(items)
print(random_item)

# Question 14: Write a Python program to find the second smallest number in a list.

lst = [11, 5, 3, 133, 3, 54, 100, 666, 1, 12]
lst.sort()
a = lst[1]
print('this is small:', a)


# Question 15: Write a Python program to get unique values from a list

lst = [11, 5, 3, 133, 3, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 454, 100, 666, 1, 1, 12]
a = set(lst)
b = a
my_list = list(b)
print(my_list)


# Question 16: Write a Python program to check whether a list contains a sub list

my_list = [1, 2, 3, [4, 5], 6, 7]
sub_list = [4, 5]
if sub_list in my_list:
    print("The list contains the sub list")
else:
    print("The list does not contain the sub list")


# Question 17: Write a Python program to split a list into different variables.


my_list = [1, 2, 3, 4, 5]

a, b, c, d, e = my_list

print(a)
print(b)
print(c)
print(d)
print(e)


# Question 19: Write a Python program to create a tuple with different data types.


my_tuple = ("apple", 1, 2.5, True)
print(my_tuple)


# Question 20: Write a Python program to create a tuple with numbers.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)


# Question 21:write a python program to convert a tuple to string.

my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
my_string = ''.join(my_tuple)

print(my_string)


# question 22:write a python program to check whether an element exists within a tuple.

tup1 = ("h", "e", "m", "l", "a", "t", "a")
print("e" in tup1)
print(5 in tup1)


# question 23:write python program to find length of a tuple.

tup1 = (2, 22, 44, 66, 88, 122, 142)

lt = len(tup1)
print(lt)


# question 24:write a python program to convert list to tuple.

list1 = [5, 10, 7, 4, 15, 3]
tup1 = tuple(list1)
print(tup1)


# question 25: write a python program to reverse a tuple.

t = (0, 1, 2, 3)

t_reversed = t[::-1]

print(t_reversed)


# question 26:write a python program to replace last value of tuple in a list.

l1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t1[:-1] + (100,) for t1 in l1])


# question 27:write a python program to find the repeated items of a tuple.

tup1 = (1, 2, 3, 4, 5, 2, 4, 6)

repeated_items = []
for item in tup1:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("The repeated items in the tuple are:", tuple(repeated_items))


# question 28

def removet(li):
    li = [num for num in li if num]
    return li


li = [(), ('Studytonight', '1', '2'), (), ('3', '4', '5', '6')]
print(removet(li))


# question 29:Write a Python program to unzip a list of tuples into individual lists.

list1 = [(1, 2), (3, 4), (8, 9)]
print(list(zip(*list1)))


# question 30:Write a Python program to convert a list of tuples into a dictionary.

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print(Convert(tups, dictionary))


# Question 32: Write a Python script to sort (ascending and descending) a dictionary by value.

y = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}

l = list(y.items())
l.sort()
print('Ascending order is', l)

l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)

dict = dict(l)
print("Dictionary", dict)


# question 33:Write a Python script to concatenate following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)


# question 34:Write a Python script to check if a given key already exists in a dictionary.

dict1 = {'apple': 1, 'banana': 2, 'orange': 3}

key = 'apple'
if key in dict1:
    print(f"{key} exists in the dictionary.")
else:
    print(f"{key} does not exist in the dictionary.")

    # question 35:How Do You Traverse Through A Dictionary Object In Python?

site_stats = {'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}
for k, v in site_stats.items():

    print("The key is: %s" % k)

    print("The value is: %s" % v)

    print("++++++++++++++++++++++++")


# question 37:Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dict1 = {}

for i in range(1, 16):
    dict1[i] = f"value {i}"

print(dict1)


# question 38: Write a Python program to check multiple keys exists in a dictionary.

student = {'name': 'hemlata', 'class': 'V', 'roll_id': '2'}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'hemlata'})
print(student.keys() >= {'roll_id', 'name'})


# question 39:Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


# question 40:Write a Python program to map two lists into a dictionary

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]


print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))


res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}


print("Resultant dictionary is : " + str(res))


# question 41:Write a Python program to combine two dictionary adding values for


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

for key in d2:
    if key in d1:
        d2[key] = d2[key] + d1[key]
    else:
        pass

print(d2)


# question 42:Write a Python program to print all unique values in a dictionary.

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 4, 'f': 3}

unique_values = set(dict1.values())

print("Unique values in the dictionary are:")
for value in unique_values:
    print(value)


# question 44:Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.

d = {'1': ['a', 'b'], '2': ['c', 'd']}

for x in d['1']:
    for y in d['2']:
        print(x + y)

        # question 45:Write a Python program to find the highest 3 values in a dictionary


my_dict = {'T': 23, 'U': 22, 'T': 21, 'O': 20, 'R': 32, 'S': 99}
k = Counter(my_dict)

high = k.most_common(3)
print("Dictionary with 3 highest values:")
print("Keys : Values")
for i in high:
    print(i[0], " : ", i[1], " ")

    # question 46:Write a Python program to combine values in python list of dictionaries.


item_list = [{'item': 'item1', 'amount': 400}, {
    'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)

# question 47:Write a Python program to create a dictionary from a string.

string = 'w3resource'

result = {}

for char in string:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)


# question 48:Write a Python function to calculate the factorial of a number (a nonnegative

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is only defined for nonnegative integers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


factorial(5)


# question 49:Write a Python function to check whether a number is in a given range.


def check_range(num, start, end):
    if num in range(start, end+1):
        return True
    else:
        return False


check_range(15, 1, 10)


# quetion 50:Write a Python function to check whether a number is perfect or not.

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


print(perfect_number(6))


# question 51:Write a Python function that checks whether a passed string is palindrome or not.

a = "malayalam"

b = ""
for i in a:
    b = i + b
if (a == b):
    print("Yes")

else:
    print("No")


# Question 53: How can you pick a random item from a list or tuple?


my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)

print(random_item)


# Question 54: How can you pick a random item from a range?


random_number = random.randrange(1, 11)

print(random_number)


# Question 55: How can you get a random number in python?


random_number = random.randint(1, 100)
print(random_number)


# Question 58: Write a Python program to read a random line from a file.


with open('file.txt', 'r') as f:
    lines = f.readlines()
    random_line = random.choice(lines)
    print(random_line)

    # Question 59: Write a Python program to convert degree to radian


degrees = 45
radians = degrees * math.pi / 180

print(radians)


# Question 60: Write a Python program to calculate the area of a trapezoid

height = 5
base1 = 7
base2 = 12

area = 0.5 * (base1 + base2) * height

# Question 61: Write a Python program to calculate the area of a parallelogram

base = 10
height = 6

area = base * height

print(area)


# Question 62: Write a Python program to calculate surface volume and area of a cylinder


radius = 3
height = 8

sa = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
print("Surface Area:", sa)

v = math.pi * radius ** 2 * height
print("Volume:", v)


# Question 63: Write a Python program to returns sum of all divisors of a number

def sum_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


num = 24
print(sum_divisors(num))


# question 65:Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

numbers = [2.5, 7.8, 1.2, 5.6, 9.1]

max_num = max(numbers)
print("Maximum number is:", max_num)

min_num = min(numbers)
print("Minimum number is:", min_num)
