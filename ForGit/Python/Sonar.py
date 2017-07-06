#Sonar
import random
import time

class Game():
    def __init__(self):
        self.board = list(range(20))
        self.treasure_list = []


        pass

    def draw_new_board(self):
        for i in self.board:
            print(i)

    def run(self):
        import sys
        print("Welcome to Sonar! the game where you place sonar booms in the water and try to find the treasure")
        self.newgame()
        self.play_again()
        
                
    def play_again(self):
        print ("Would you like to play again?" )
        t =input()
        if t == "N":
               import sys;  sys.exit
        elif t == "Y":
            self.newgame()
        else:
            self.play_again()
        
    

    def make_guess(self):
       #remove all the print functions later
       #make guess takes two numbers and checks them to see if they are valid and then
       # puts those two numbers into variables (part1, part2)
       #then we check with check_guess whcih is another method. 
        print("please enter 2 values separated by a space")
        Guess = input()
        part1 = ""
        part2 = ""
        v = 0

        if len(Guess) < 3:
            print("I'm sorry you have to enter 2 values separated by a space")
            self.make_guess()

        
        for i in range(len(Guess)):
            if Guess[i] == " ":
                v = i +1
                break
            else:
                part1 += Guess[i]
             
        
        for i in range(len(Guess) -v):
            part2 += Guess[v+i]
        
        if len(part2) ==0:
            print("I'm sorry you have to enter a second number")
            self.make_guess()
   #stripping the spaces at the end of the number
        
        


        if part1.isdigit():
               part1 = int(part1)
        else:
               print("first entry not a number")
               self.make_guess()
               return
            

        if int(part1) < 0:
            print ("first number must be between 1 and 15")
            self.make_guess()
            return
        elif int(part1)> 15:
            print("first number must be between 1 and 15")
            self.make_guess()
            return
        else:
            pass
     
    

        if type(int(part2)) == type(5):
           
            part2 = int(part2)
        else:
            
            print('second entry not a number')
            
            
            self.make_guess()
            return
        if int(part2) < 0:
            print("second number must be between 1 and 60")

            self.make_guess()
            return
        elif int(part2) > 60:
            print("second number must be between 1 and 60")
            self.make_guess()
            return
        else:
            pass
        self.check_guess(int(part1),int(part2))
        

    def check_guess(self, x, y):
        print("you drop a sonar device into the deep and wait anxiously....")
        time.sleep(3)

        dist = 0
        #what the distance is if it's too far away to calculate
        x = int(x)
        y = int(y)
     

        if (x,y) in self.treasure_list:
            self.treasure_list.remove((x,y))
            print (self.treasure_list)
            self.board[x+2] = self.board[x+2][:(y+2)] + "X" + self.board[x+2][(y+3):] 
            
        else:
            #calculating the distance to each treasure chest and figuring out which is the
            #greater distance EXCEPT if the distance is greater than 9 in which case we don't count

            for each_treasure in self.treasure_list:
                
                sub_dist = 0
                
                xdist = abs(each_treasure[0] -x)
                ydist = abs(each_treasure[1] -y)

                if xdist >= ydist:
                    sub_dist = xdist
                else:
                    sub_dist = ydist
                

                if sub_dist > 9:
                    pass
                elif dist == 0:
                    dist = sub_dist
                    
                elif sub_dist < dist:
                    dist = sub_dist
                    
                else:
                    pass
           
            #now update the board to reflect that there is a sonar there with the dist
            self.board[int(x)+2] = self.board[x+2][:(y+2)]  + str(dist) + self.board[x+2][(y+3):]
            

    def newgame(self):
            #construct line 1-19
        self.board[0] = " " * 13 + "1" + (" " * 9) + "2" + (" " * 9) + "3" + (" " * 9) + "4" + (" " * 9) + "5" + (" " * 11)
        self.board[1] = "                                                                "
        self.board[2] = "   123456789012345678901234567890123456789012345678901234567890 "
        self.board[3] = " 1 ~`~~~```~~~~`~`~~`~``~`~~```~`~`~~`~`~~~~~~`~`````~`~~`~~~~` 1"
        self.board[4] = " 2 `~``~``~~~`~``~`~`~``~`````~~~~~~~~~`~`~~`~``~~~~~```~~`~``` 2"
        self.board[5] = " 3 ``~`~~``~`~``~`~`~`~~`~`~~`~`~``~~~`~``~````~``````~~~~``~`` 3"
        self.board[6] = " 4 ``~~`~~~``~``~~````~`~`~`~``~~~``~~```~`~~`~~`~`~`~~`~~~~``` 4"
        self.board[7] = " 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5"
        self.board[8] = " 6 ``~~`````~~~~`~`~~~```~~~~`~~`~~`~~```~~`~~~`~~~``~`~~~``~~~ 6"
        self.board[9] = " 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7"
        self.board[10] =" 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`~`````~`~~```~`~~~~` 8"
        self.board[11] =" 9 ~```~~`~`~``~``~~``~``~```~`~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9"
        self.board[12] ="10 ```~`~```~``~``~`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10"
        self.board[13] ="11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11"
        self.board[14] ="12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12"
        self.board[15] ="13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13"
        self.board[16] ="14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14"
        self.board[17] ="15 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 15"
        self.board[18] ="   123456789012345678901234567890123456789012345678901234567890  "
        self.board[19] =" " * 12 + "1" + (" " * 9) + "2" + (" " * 9) + "3" + (" " * 9) + "4" + (" " * 9) + "5" + (" " * 11)

        # create treasure
        #note the translation for this stuff is [+2][+2] with a "natural " shift of one on each side
        #due to the creation of the 

        treasure1 = (random.randint(1,15), random.randint(1,60))
        treasure2 = (random.randint(1,15), random.randint(1,60))
        treasure3 = (random.randint(1,15), random.randint(1,60))

        self.treasure_list = [treasure1, treasure2, treasure3]


        #check to make sure treasures are unique
        if treasure1 in [treasure2, treasure3]:
            self.newgame()
        elif treasure2 == treasure3:
            self.newgame()

        else:
            pass
        self.number_of_guesses = 15  
        while self.number_of_guesses >= 0:
            self.draw_new_board()

            print("You have " + str(self.number_of_guesses) + " guesses left.")
            
            self.make_guess()
            #check to see if you have won
            if self.treasure_list == []:
                print("You have won!!!!!")
                print("congratulations!!!!")
                self.number_of_guesses = 0 
            else:
                self.number_of_guesses -= 1
            if self.number_of_guesses  < 0:
                print("I'm sorry, you've lost.....") 

       






t = Game()
t.run()


