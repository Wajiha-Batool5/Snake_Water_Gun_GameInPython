'''
1 is for snake
-1 is for water
0 is for gun
'''
import random

computer=random.choice([1,-1,0])
yourChoice=input("Enter your choice: ")
yourDict={'s':1,'w':-1,'g':0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}
you=yourDict[yourChoice]

print(f'You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}')

if (computer==you):
    print("It's a draw.")
else:
    if (computer==-1 and you==1):
        print('You win!')
    elif (computer==-1 and you==0):
        print('You lose!')
    elif (computer==1 and you==0):
        print('You win!')
    elif (computer==1 and you==-1):
        print('You lose!')
    elif (computer==0 and you==1):
        print('You lose!')
    elif (computer==0 and you==-1):
        print('You win!')