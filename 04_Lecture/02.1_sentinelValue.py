"""
Program: Sentinel Value Example - Average Calculation
Date: 12/05/2024
Description:
    This program calculates the average of a series of positive integers entered by the user, 
    ignoring values greater than or equal to 20. The input process stops when the user enters 
    a negative value (-1 acts as the sentinel). If no valid values are entered, the program 
    informs the user that no list was created.

Usage:
    - Run the program.
    - Enter positive integers less than 20 to include in the calculation.
    - Enter -1 (or any negative value) to terminate the input process.

Input:
    - Positive integers (< 20) for valid inputs.
    - Any negative value to end the input.

Output:
    - The average of the entered values (excluding values >= 20).
    - A message if no valid inputs were provided.

Example:
    Enter the number or negative values to finish: 10
    Enter the number or negative values to finish: 15
    Enter the number or negative values to finish: 25
    Enter the number or negative values to finish: -1
    The average of these 2 values is 12.5
"""


#code
positiveInteger = 0
totalSum = 0
numCount = 0

while positiveInteger >= 0 :     #means positiveInteger can not be less than zero(0)
    positiveInteger = int(input("Enter the number or negative values to finish: "))
    if positiveInteger <20 :
        totalSum += positiveInteger
        numCount += 1

if numCount > 0:
    average = totalSum / numCount
    print(f"The average of these {numCount} values is {average}")
else:
    print("The list has not been created")
