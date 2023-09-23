
def checkSum():
    a=int(input("Enter first num: "))
    b=int(input("Enter second num: "))

    if (a == b) or (a- b == 5) or (b-a == 5) or (a+b == 5) : 
        print("True");
    else:
        print('False')

checkSum()
