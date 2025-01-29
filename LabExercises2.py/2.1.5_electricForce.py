from math import pi

constant = 8.854e-12  #10 to the power negative 12
q1 = float(input("Enter the charge for particle 1(in C): "))
q2 = float(input("Enter the charge for particle 2(in C): "))
r = float(input("Insert the distance between the charges(in m): "))
  
#compute the force 
relativeForce = (q1 * q2) / (4 * pi * constant * r ** 2)

print(f"Between the two charges the relative force is: {relativeForce:.2e} N")
