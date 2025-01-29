#OPTION 1: treat the number as a 5-character string
fiveDigit = int(input("Inser the five digit Number: "))
fiveDigit = str(fiveDigit)  #Conver the number into string 

for indx in range(len(fiveDigit)):
    print(fiveDigit[indx])


#OPTION 2: use Division and Modulo of powers of 10
num = int(input("Enter a 5 digit integer: "))

print((num // 10000) % 10)
print((num // 1000) % 10)
print((num // 100) % 10)
print((num // 10) % 10)
print(num % 10)
