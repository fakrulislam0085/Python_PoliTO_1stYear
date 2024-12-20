cityName = "Roma"

for letter in cityName :
    print(letter, end=" ")

#range container
num = 5

print()
for i in range(num) :       #num excluded, 0 to num-1
    print(i, end=" ")

print()
for i in range(1, num) :    #num excluded, initialization, condition   
    print(i, end=" ")

print()
for i in range(2, num, 2) :    #initialization, condition, increment/decrement
    print(i, end=" ")

print()
for i in range(num, 0, -1) :
    print(i, end=" ")