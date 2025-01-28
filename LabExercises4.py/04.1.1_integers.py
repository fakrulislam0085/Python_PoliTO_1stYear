num = input("Enter a Number: ")
endOfInput = ""
s = 0
evenValueCnt = 0 
OddValueCnt = 0
mx = int(num)
mn = int(num)

while num != endOfInput :
    num = int(num) 

    #task 1
    s += num 
    print(f"Partial Sum: {s}")  

    #task 2- printing max and min  
    if num <= mn :
        mn = num    
    if num >= mx :
        mx = num 
    print("Maximum value among all of the values:", mx)
    print("Minimum Value among all of the values:",mn)   


    #task 3- odd and even value count
    if num %2 == 0 :
        evenValueCnt += 1 
    else :
        OddValueCnt += 1 
    print("Number of even values:", evenValueCnt)
    print(f"Number of Odd values: {OddValueCnt} \n")

    num = input("Enter a Number: ")
