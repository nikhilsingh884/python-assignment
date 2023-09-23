# question 19:Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
# 'not'...'poor'substring with 'good'. Return the resulting string.

string = "i know you are not poor"
a = string.find('not')
b = string.find('poor')

if a != -1 and b != -1 and a < b:
    print(string[:a] + 'good' + string[b+4:])
else:
    print(string)

# question 20: Write a Python function that takes a list of words and returns the length
# of the longest one.


def list(a, b):
    if len(a) > len(b):
        print(len(a))
    if len(b) > len(a):
        print(len(b))


list('python', 'zoo')


# question 21: Write a Python function to reverses a string if its length is a multiple of 4.

a = input()
if len(a) % 4 == 0:
    print(a[::-1])
else:
    print(a)

    # question 22:Write a Python program to get a string made of the first 2 and the last 2
# chars from a given a string. If the string length islessthan 2,return instead
# of the empty string.
# o Sample String:w3resource'
# o Expected Result: 'w3ce'
# o Sample String: 'w3'
# o Expected Result: 'w3w3'
# o Sample String: ' w'
# o Expected Result: Empty String

s = input('enter the characters')

if len(s) > 2:
    b = s[:2] + s[-2:]
    print(s)
else:
    print('')

    # question 23:Write a Python function to insert a string in the middle of a string.

a = input('enter a string you want to change :')

b = input("enter a word with you want to add in center :")

c = a.split()
d = len(c) // 2

x = c[:d] + [b] + c[d:]

x = ' '.join(x)

print(str(x))
