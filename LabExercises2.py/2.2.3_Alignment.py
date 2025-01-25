num1 = int(input("Insert the first Number:"))
num2 = int(input("Insert the second Number:"))

sum = num1 + num2
diff = num1 - num2
product = num1 * num2 
average = sum / 2
distance = abs(num1 - num2)
mx = max(num1, num2)
mn = min(num1, num2)


print(f"{'Summation:':<15}{sum:>10}")
print(f"{'Difference:':<15}{diff:>10}")
print(f"{'Product:':<15}{product:>10}")
print(f"{'Average:':<15}{average:>10}")
print(f"{'Distance:':<15}{distance:>10}")
print(f"{'Maximum:':<15}{mx:>10}")
print(f"{'Minimum:':<15}{mn:>10}")

'''
:<15 ensures that the labels take up 15 characters, aligned to the left.
:>10 aligns the values to the right within a 10-character width, creating the desired spacing.'''