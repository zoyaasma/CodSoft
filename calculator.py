# basic calculator
#input two operands
from random import *
a=int(input("enter 1st operand"))
b=int(input("eneter second operand"))
print("declare the operators like ''+','-','*','/','%''")
c=['+','-','*','/','%',]
def calc():
    ch=choice(c)
    if ch=='+':
        print("add",a+b)
    elif ch=='-':
        print("sub",a-b)
    elif ch=='*':
        print("mul",a*b)
    elif ch=='/':
        print("div",round(a/b))
    elif ch=='%':
        print("mod",a%b)
    else:
        pass
calc()
while(1):
    ch=int(input("enter 1 if u want to continue,else 0"))
    if ch==1:
        calc()
    else:
        break
    
    

