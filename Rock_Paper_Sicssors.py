from termcolor import colored as color
import random
def main() :
    numplayed = 0
    g1win = 0
    g2win = 0
    print(color("Wellcome to Rock Paper Sicssors" , "green"))
    print("\n")
    while numplayed < 3 :
        print(f"Game played : {numplayed}")
        g1 = random.randint(0,2)
        
        print(color("""
            1.Rock
            2.Paper
            3.Scissors  
            """ , "magenta"))
        
        g2 = input(color("Enter your action ==>> " , "cyan"))
        lrock = [1 , "1" , "rock" , "Rock"]
        lpaper = [2 , "2" , "paper" , "Paper"]
        lscissors = [3 , "3" , "scissors" , "scissors"]
        
        # check gamer1 value
        if g1 == 0 :
            g1 = "rock"
        elif g1 == 1 :
            g1 = "paper"   
        elif g1 == 2 :
            g1 = "scissors"  
        else : 
            print(color("Please enter correct value !!!!!!!!!!!" , "red"))
         
         
        # check gamer2 value
        if g2 in lrock :
            g2 = "rock" 
        elif g2 in lpaper :
            g2 = "paper"   
        elif g2 in lscissors :
            g2 = "scissors"
        
        
            
        #Check gamer's value
        if g1 == "rock" : 
            if g2 == "rock" :
                print(color("Equal" , "yellow"))

            elif g2 == "paper" :
                print(color("You win!!!!!!!" , "green"))
                numplayed += 1
                g2win += 1
            elif g2 == "scissors" :
                print(color("You lose !!!!!" , "red"))
                numplayed += 1
                g1win += 1
                
                
        elif g1 == "paper" :
            if g2 == "paper" :
                print(color("Equal" , "yellow"))

            elif g2 == "scissors" :
                print(color("You win !!!!" , "green"))
                numplayed += 1
                g2win += 1
            elif g2 == "rock" :
                print(color("You lose !!!!" , "red"))
                numplayed += 1
                g1win += 1
        
        elif g1 == "scissors" :
            if g2 == "scissors" :
                print(color("Equal" , "yellow"))
                
            elif g2 == "rock" :
                print(color("You win !!!!" , "green"))
                numplayed += 1
                g2win += 1
            elif g2 == "paper" :
                print(color("You lose !!!!" , "red"))
                numplayed += 1
                g1win += 1
        # End Check gamer's value
                
    # Check who win
    if g1win == 3 :
        print(color("You lose the game!!!!" "red"))
    elif g1win == 2 :
        print(color("You lose the game!!!" , "red"))
    else :
        print(color("You win the game !!!!" , "green"))
        
    print("The End")
        
                
                

main()