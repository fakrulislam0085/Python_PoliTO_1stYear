#boolean not operator can inverse our output to an opposite direction

attending = True
print(not attending)


grade = 17
if not (grade < 18):
    print("passing")


number = 200
if number > 0:
    print("True")
m = 85
if not m < 0:  #m > 0 but as we used 'not' variable here so it executes the output
    print("True")



#Combining not with Other Logical Operators
if not attending or grade < 18 :
    print("Drop!")
if attending and not(grade < 18) :
    print("Stay!")