# question 1:What is File function in python? What is keywords to create and write file.

# A file is a container in computer storage devices used for storing data.

# When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:

# Open a file
# Read or write (perform operation)
# Close the file

open('fun1.txt','x')
f1=open('fun1.txt','w')
f1.write("name ")
f1.close()
f2=open('fun1.txt','w')
f2.write("python is a high programming lanaguage")
f2.close()

#question 2: Write a Python program to read an entire text file.

f3=open('fun.txt','r')
d=f3.read()
f3.close()
print(d)

#question 3: Write a Python program to append text to a file and display the text.
y1=open('fun.txt','a')
y1.write('and also open source')
y1.close()

y1=open('fun.txt','r')
q=y1.read()
y1.close()
print(q)

# MangoOrangeAppleLemonand also open source

q1=open('fun.txt','w')
q1.write("""python is high programming language\na also a open source language\npython is a high programming language""")
q1.close()

q1=open('fun.txt','r')
d=q1.read()
q1.close()
print(d)

# python is high programming language
# a also a open source language
# python is a high programming language

f5=open('fun.txt','r')
res=f5.readline()
f5.close()



# question 4:Write a Python program to read a file line by line and store it into a list

f5=open('fun.txt','r')
res=f5.readlines()
f5.close()
print(res)

# question 5:Write a Python program to read a file line by line and store it into a variable.

f5=open('fun.txt','r')
a=f5.readline()
b =f5.readline()
c=f5.readline()
f5.close()
print(a,b,c)

# question 6:Write a python program to find the longest words.

def largestWord(s):
    s = sorted(s, key = len)
 
    print(s[-1])
    
if __name__ == "__main__":
 
    
    s = "be confident and be yourself"

    l = list(s.split(" "))
    largestWord(l)

# question 7:Write a Python program to read last n lines of a file

f5=open('fun.txt','r') 
lastline=f5.readlines()[-1]
print(lastline)

# question 8:Write a Python program to read a file line by line and store it into a list

f5=open('fun.txt','r')
lines=f5.read().splitlines()

print(lines)
f5.close()

# question 9:Write a Python program to read a file line by line store it into a variable.
f5=open('fun.txt','r')
lines=f5.read().splitlines()

print(lines)
f5.close()
f5=open('fun.txt','r')
lines=f5.read().splitlines()

print(lines)
f5.close()


# question 10: Write a Python program to count the number of lines in a text file.

f5=open('fun.txt','r')
lines=len(f5.readlines())

print(lines)
f5.close()

# qestion 11:Write a Python program to count the frequency of words in a file.
count=0
f5=open('fun.txt','r')
for line in f5:
    words=line.split(" ")
    count += len(words)
print(str(count))
f5.close()

# qestion 12:Write a Python program to write a list to a file.
items = ['Mango' , 'Orange' , 'Apple' , 'Lemon']
file = open('fun.txt','w')
file.writelines(items)
file.close()

file=open('fun.txt','r')
file.read()

# question 13: Write a Python program to copy the contents of a file to another file.

file1 = open("fun.txt", "r")
file2 = open("fun1.txt", "w")
l = file1.readline()

while l:
    file2.write(l)
    l = file1.readline()
file1.close()
file2.close()


# question 20 Here's an example Python program that prompts the user to enter an odd number, 
# and raises an exception if they enter an even number:

try:
    x = int(input("Enter an odd number: "))
    if x % 2 == 0:
        raise ValueError("Invalid input: Please enter an odd number")
    else:
        print("You entered an odd number:", x)
except ValueError as ve:
    print(ve)

# question 23:Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())


# question 24:Write a Python class named Circle constructed by a radius and two methods which will 
#compute the area and the perimeter of a circle

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# question 25:Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Inheritance is a concept in object-oriented programming (OOP) where one class 
# (called the child or subclass) can inherit the attributes and methods of another
# class (called the parent or superclass).
# The child class can then use these inherited attributes and methods,
# as well as add new attributes and methods of its own.


# he __init__ method in Python is a special method that gets called when an instance of a class is created. 
# It is used to initialize the attributes of the instance with the values passed to the constructor.

class Animal:
    name = ""
    
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def display(self):
        print("My name is ", self.name)

labrador = Dog()
labrador.name = "maggie"
labrador.eat()
labrador.display()


