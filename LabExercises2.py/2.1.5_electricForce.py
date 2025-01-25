q1 = float(input("insert charge 1: "))
q2 = float(input("insert charge 2: "))
r = float(input("Insert the distance between the charges: "))

constant = 4 * 3.1416 * (8.854 * 1e-12)   #10 to the power negative 12
calculation1 = q1 * q2 
calculation2 = r * constant

relativeForce = calculation1 / calculation2

print(relativeForce)
