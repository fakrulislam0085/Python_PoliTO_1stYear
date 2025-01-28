#int and int
a = 1
b = 1
if a == b:
    print("Both are equal:",type(a))
else :
    print("Type-A:",type(a),'\n'+"Type-B:",type(b))


#int and float
print()
c = 1
d = 1.52        #try to set the value of d = 1.00 and run the code
if c == d:
    print("Both are equal:", type(c))
else :
    print("Type-C:",type(c),'\n'+"Type-D:",type(d))     #to avoid extra space in front of second line, use concatenation


#float and float
print()
from math import *  #imports all mathematical functions
d = 2.00
e = sqrt(4)
if d == e:
    print("Both are equal:", type(d))
else :
    print("Type-D:",type(d),'\n',"Type-B:",type(e))


#string and int
print()
f = '1'
g = 1
if f == g:
    print("Both are equal:", type(f))
else :
    print("Type-F:",type(f),'\n'+"Type-G:",type(g))


#string and string
print()
h = 'ciao'
i = 'ciao'
if h == i:
    print("Both are equal:", type(h))
else :
    print("Type-A:",type(h),'\n'+"Type-B:",type(i))

