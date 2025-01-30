Number = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sum_even = 0
sum_odd = 0

for num in Number:
    if num % 2 == 0:
        sum_even += num
     
    else:
        sum_odd += num

print ("Sum of Even Number:", sum_even)
print ("Sum of Odd Number:", sum_odd)

    
