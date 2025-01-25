R1 = int(input("Insert the resistance1: "))
R2 = int(input("Insert the resistance2: "))
R3 = int(input("Insert the resistance3: "))

#For series connection 
R = R1 + R2 + R3
print("Series resistance: ", R)

#For parallel connection
R = (1/R1) + (1/R2) + (1/R3)
print("Pallel resistance: ", 1/R)


