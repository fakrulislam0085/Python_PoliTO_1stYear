def boxString(contents) :
    n = len(contents)
    
    if n == 0:
        return      #this return will terminate the function with immediately if n==0
    
    print("-" * (n+2))
    print("!" + contents + "!")
    print("-" * (n+2))
    return          #using Return function without any value

boxString("Hello")