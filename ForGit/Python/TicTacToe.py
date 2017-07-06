
import random


class Game():
    def __init__(self):
        #just put whether the board is full to false and run the new game
        

        self.new_Game()
        
    def make_Board(self):
        #designing the board

        self.board = list(range(3))

        for i in range(3):
            self.board[i] = list(range(3))

        for i in range(len(self.board)):
          
            for j in range(len(self.board[i])):
                
                
                self.board[i][j] = " "
        self.empty_spaces = 9
        self.boardFull = False
    def draw_Board(self):
        #putting the board on the screen
        
        print("-" * 7)

        print("|" + self.board[0][0] + "|"
              + self.board[0][1] + "|" + self.board[0][2] + "|")

        print("-" * 7)
        print("|" + self.board[1][0] + "|"
              + self.board[1][1] + "|" + self.board[1][2] + "|")

        print("-" * 7)
        print("|" + self.board[2][0] + "|"
              + self.board[2][1] + "|" + self.board[2][2] + "|")
        print("-" * 7)
    def pick_X_O(self):
        #do you want to be X's or O's player choice 
        print("please pick X's or O's")
        choice = input().upper()
        if choice == "X":
            self.player_choice = choice
            self.computer_choice = "O"
            pass
        elif choice == "O":
            self.player_choice = choice
            self.computer_choice = "X"
        else:
            print("I'm sorry I didn't understand your response."
                  + " Please pick X's or O's and hit enter")
            self.pick_X_O()


        
    def who_Goes_First(self):
        b = random.randint(0,1)
        if b == 1:
            self.whose_turn = "Player"
            print("you go first")
        elif b == 0:
            self.whose_turn = "Computer"
            print("computer goes first") 

        else:
            print("something went very wrong here")
    def turn(self):
        
        if self.whose_turn == "Computer":
            self.computer_Moves()
            self.whose_turn = "Player" 

        elif self.whose_turn == "Player":
            self.player_Moves()
            self.whose_turn = "Computer"
            
        else:
            print("something is odd, it's no one's turn")
            pass
    
        if self.empty_spaces <= 0:
            self.boardFull = True
        else:
            pass
        
    def computer_Moves(self):
        valid_moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == " ":
                    valid_moves.append((i,j))
                else:
                    pass
      
        corner_moves = []
        for each in [(0,0), (0,2), (2,0), (2,2)]:
            if each in valid_moves:
                corner_moves.append(each)
            else:
                pass

                
        
       #check to see if the computer can win next turn and does it if it does     
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.computer_choice
                    if self.check_Winner():
                        self.board[i][j] = self.computer_choice
                        self.draw_Board()
                        print("I'm sorry, the computer won")
                        self.at_Games_End()
                    else:
                        self.board[i][j] = " "
                        pass
                else:
                    pass 
       #check to see if the player can win next turn and blocks if able.
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.player_choice
                    if self.check_Winner():
                        self.board[i][j] = self.computer_choice
                        self.empty_spaces -= 1

                        return
                    else:
                        self.board[i][j] = " "
                        pass
                else:
                    pass
                
      #if you get to this point there is no crucial moves, then make a corner move
        
        if corner_moves != []:
            b = random.choice(corner_moves)
            self.board[b[0]][b[1]] = self.computer_choice
            self.empty_spaces -= 1
            
            return
    #if you can't make a corner move make a center move 
        elif self.board[1][1] == " ":
            self.board[1][1] = self.computer_choice
            self.empty_spaces -= 1
            
    #otherwise just make a random move. 
        else:
            b =random.choice(valid_moves)
            self.board[b[0]][b[1]] = self.computer_choice
            self.empty_spaces -= 1
         

    def player_Moves(self):
        self.draw_Board()
        print("select 1 through 9 with 1 being the top left square and 9 being the bottom right square")
        t = input()[0]

        if t.isdigit():
            pass 

        else:
            
            print("I'm sorry you didnt input a number between 1 and 9") 
            self.player_Moves()
        
        if int(t) < 4:
            x = 0 
        elif int(t) < 7:
            x = 1
        elif int(t) < 10:
            x = 2 
        else:
            print("I'm sorry you didnt input a number between 1 and 9") 
            self.player_Moves()
        y = (int(t)-1)%3

     

        if self.board[x][y] == " ":
            self.board[x][y] = self.player_choice
            self.empty_spaces -= 1
        else:
            print("this square is occupied, please pick another square")
            self.player_Moves()
        if self.check_Winner():
            print("Congratulations, you have won the game!!")
            self.at_Games_End()
        else:
            pass
    def at_Games_End(self):
        print("Do you want to play again? Y N")
        b = input()[0].upper()
        if b =="N":
            import sys; sys.exit()
        elif b =="Y":
            self.new_Game()
        else:
            print("I'm sorry, your input was something weird" )
            self.At_games_end()
        
    def check_Winner(self):
        
        #third time around, erased all code adn starting over
        #check the rows and columns
        

        for i in range(3):
            if len(set(self.board[i])) == 1:
                   if self.board[i][0] == " ":
                       pass
                   else:
                       return True
            elif len(set([self.board[0][i],self.board[1][i],self.board[2][i]] )) == 1:
                   if self.board[0][i] == " ":
                       pass
                   else:
                       return True
            else:
                   pass
        Diag1 = [self.board[1][1] , self.board[0][0], self.board[2][2]]
        Diag2 = [self.board[1][1] , self.board[0][2], self.board[2][0]]
        if len(set(Diag1) )== 1:
            if Diag1[0] != " ":
                   return True
            else:
                   pass
        else:
            pass
        if len(set(Diag2)) == 1:
            if Diag2[0] != " ":
               return True
            else:
                   pass
        else:
                pass
          

        return False


    def new_Game(self):
        self.make_Board()
        self.draw_Board()
        self.pick_X_O()
        self.who_Goes_First()
        while self.boardFull == False:
                     self.turn()
        self.draw_Board()
        print('The board is full and the game is ended.')
        self.at_Games_End()                 
      
    


        
g = Game()
g
