num1 = int(input("Insert the first Number:"))
num2 = int(input("Insert the second Number:"))

sum = num1 + num2
diff = num1 - num2
product = num1 * num2 
average = sum / 2
distance = abs(num1 - num2)
mx = max(num1, num2)
mn = min(num1, num2)


print(f"summation: {sum}\ndifference: {diff}\nProduct: {product}\nAverage: {average}\nDistance: {distance}\nMaximum: {mx}\nMinimum: {mn}")