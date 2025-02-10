Number = int(input("Enter the number of terms: "))

first, second = 0 , 1

print("Fibonacci Series:", end=" ")

for i in range(1, Number + 1):
    print(first, end=" ")
   
    next_term = first + second
    first = second
    second = next_term

print()