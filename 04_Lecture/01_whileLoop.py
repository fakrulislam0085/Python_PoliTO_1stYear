#This program is an example of while loop

i = 0
total = 0

while total < 10:
    i = i+1
    total = total + i
    print(i, total)


#second example
count = 0
ok = True

while count<10 and ok :
    a = int(input("insert the number: "))
    if a == 0:
        ok = False
    print(f'Number {count +1} = {a}')
    count = count + 1