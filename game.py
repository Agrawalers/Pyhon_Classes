import random
win=0
lost=0
count=0
def play_Game():
    
    global win,lost,count
    count+=1
    
    attempt=5
    list=["red","blue","white","black","green","yellow","purple","pink","brown"]
    select=random.choice(list)
    for i in range(1,attempt+1):
        
        
        attempt-=1
        color=input("Enter the name of color:-")
        if color in list:
            if(color==select):
                
                print("You won the game")
                print("Attempts needed:",5-attempt)
                win+=1
                break
            else:
                print("Your guess was wrong")
                print("Number of attempts left",attempt)
            
                
        else:
            print("Enter valid color")
        if(attempt==0 and color!=select):
                    print("You have lost the game")
                    print("The color was:-",select)
                    lost+=1
                    break

    choice2 = int(input("Enter 1 to see scoreboard\n2 to play again\n3 to exit:-"))
    if(choice2==1):
        print("Number of times winned:-",win)
        print("number of times lost:-", lost)
        print("Number of times game played",count)

    elif(choice2==2):
        play_Game()        

    elif(choice==3):
        print("You exited the game")
           

    else:
        ("Enter correct number:-")
        
    return

if __name__=="__main__":
    
    print("Welcome to the color game")
    print("Please choose from given option")
    choice = int(input("Enter 1 to play \nEnter 2 to exit :-"))
    if(choice==1 ):
        play_Game()
            

    else:
        print("You exited the game")
        #kush
