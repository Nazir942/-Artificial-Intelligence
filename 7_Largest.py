number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")


def find_largest(num1, num2):
   
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return 


result = find_largest(number1, number2)
print("The largest number is:", result)