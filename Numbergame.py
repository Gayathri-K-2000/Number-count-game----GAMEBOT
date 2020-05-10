from random import *
tot1=0
tot2= 0
def player1():
    global tot1
    ch= "yes"
    while(ch=="yes"):
        num= int(input("Choose a number between 1 to 10: "))
        if(num>10):
            print("Try Again!")
            ch= input("DO YOU WANT TO CONTINUE: yes/no: ")
        else:
            tot1+=num
            if(tot1<100):
                print("Your total: ",tot1)
                player2()
            else:
                print("YOU LOOSE")       
            break
    return 

def player2():
    global tot2
    r= randint(1, 10)
    print("I choose: ",r )
    tot2+=r
    if(tot2<100):
        print("My total: ",tot2)
        player1()

    else:
        print("YOU WIN") 
    return 

if __name__=="__main__":
    
    player= int(input("-- Choose : '1' for player1 and '2' for player 2 --"))
    if(player==1):
        player1()
       
    else:
        player2()

