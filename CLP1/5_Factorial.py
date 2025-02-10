Number = int(input("Enter a number : "))

factorial = 1

if Number < 0:
    print("Factorial does not exist for negative numbers.")
elif Number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, Number + 1):
        factorial *= i

    print(f"The factorial of {Number} is {factorial}.")