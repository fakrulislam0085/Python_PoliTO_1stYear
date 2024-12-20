"""
Program: Sentinel Value Example Using String
Date: 12/05/2024
Description:
    This program demonstrates the use of a sentinel value (an empty string "") to 
    terminate a loop. The user is prompted to input numerical values continuously. 
    The program calculates and displays the total of these values once the user 
    signals the end of input by pressing 'Enter' without providing a value.

Usage:
    - Run the program.
    - Enter numerical values one at a time. 
    - Press 'Enter' on an empty input to stop the input process and display the total sum.

Input:
    - Numerical values (float or integer) as strings.

Output:
    - The sum of all entered numerical values.

Example:
    Enter Value: 10.5
    Enter the vale: 5.3
    Enter the vale: 
    Total is: 15.8
"""

#code
total = 0.00
inputStr = input("Enter Value: ")
while inputStr != "" :
    value = float(inputStr)
    total += value
    inputStr = input("Enter the vale: ")
print("Total is:",total)