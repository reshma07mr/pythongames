#without using xternal game library
#a game for man vs computer

#for random number generation
import random

#rules of game
print("Winning rules as follows:\n If rock and paper comes,paper wins.\n Paper and scissor comes,scissor wins\n Scissor and rock comes,rock wins.")

def myfunction():

    #gamebegins
    print("the choice is as follows:\n1.Paper \n2.Scissor \n3.Rock")
    choice=int(input("enter your choice:"))

    #for invalid entries
    if choice >3 or choice <1:
        print("Invalid selection made:")
        choice=int(input("enter your choice:"))
        #exit()

    #for displaying the user choice
    if choice ==1:
        print("Paper is selected")
    elif choice ==2:
        print("Scissor is selected")
    else:
        print("Rock is selected")    

    #for computer choice
    comp_choice=random.randint(1,3)
    if comp_choice ==1:
        print("Paper is selected")
    elif comp_choice ==2:
        print("Scissor is selected")
    else:
        print("Rock is selected")

    #lets play game
    if (choice ==1 and comp_choice==3) or (choice==3 and comp_choice==1):
        result=1
    elif (choice ==2 and comp_choice==1) or (choice==1 and comp_choice==2):
        result=2   
    elif (choice ==2 and comp_choice==3) or (choice==3 and comp_choice==2):
        result=3 
    else:
        result=0

    if result==choice:
        print("User wins")

    elif result==comp_choice:
        print("computer wins")

    else:
        print("game is draw")

    #for repeated gaming
    print("Do you want to continue the play ?\n 1.For next game.\n2.Exit")
    
myfunction()

'''#for repeated gaming
print("Do you want to continue the play ?\n 1.For next game.\n2.Exit")'''
entry=int(input("Enter your choice"))

if entry ==1:
    myfunction()
else:
    print("Home screen")
    exit()    