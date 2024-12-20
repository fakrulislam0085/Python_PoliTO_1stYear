#print headers
print("    x¹   x²   x³   x⁴")
print(" "*4 + '*' * 20)     #4 spaces + 20 stars

#printing row coloum
for i in range(1, 11) :
    print(f"{i**1:5} {i**2:5} {i**3:5} {i**4:5}")