#ask user to choose the input
#import random module
from random import *
print("enter avbl options '1.rocks\2.paper\3.scissors'")
def game():
    user_choice=int(input("enter"))
    #print(user_choice)
    comp_ch=randint(1,3)
    print(comp_ch)
    if(user_choice=="rock" and comp_ch=="scissors"):
        print("user wins")
    elif (user_choice=="scissors" and comp_ch=="rock"):
        print("computer wins")
    elif(user_choice==comp_ch):
        print("tie")
    elif(user_choice=="scissors" and comp_ch=="paper"):
        print("user wins")
    elif(user_choice=="paper" and comp_ch=="scissors"):
        print("computer wins")
    elif(user_choice=="paper" and comp_ch=="rock"):
        print("user wins")
    elif(user_choice=="rock" and comp_ch=="paper"):
        print("computer wins")
    else:
        pass
game()
while(1):
    ch=int(input("enter 1 if u want to continue,else 0"))
    if ch==1:
        game()
    else:
        break
    
        


