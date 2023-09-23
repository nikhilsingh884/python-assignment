num = int(input("Enter a number: "))
    
if num < 0:
        print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print(f"Factorial of {num} is: {factorial}")