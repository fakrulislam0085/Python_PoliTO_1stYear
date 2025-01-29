R1 = float(input("Insert the resistance1: "))
R2 = float(input("Insert the resistance2: "))
R3 = float(input("Insert the resistance3: "))

#For series connection 
Rs = R1 + R2 + R3
print("Series resistance: ", Rs, 'Ω')

#For parallel connection
Rp = 1((1/R1) + (1/R2) + (1/R3))
print("Pallel resistance: ", Rp, 'Ω')


