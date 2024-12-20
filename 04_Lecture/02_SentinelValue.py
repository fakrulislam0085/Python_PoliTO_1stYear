salary = 0.0
totalsalary = 0.0
monthcount = 0


while salary >= 0.00 :
    #take salary as input and then check is it a valid salary or not
    salary = float(input("Insert salary or -1 to stop the loop: "))
    if salary >= 0.00:
        totalsalary += salary
        monthcount = monthcount + 1

if monthcount > 0:
        average = totalsalary / monthcount
        print(f"Average salary is {average}")
else:
    print("No data was entered")