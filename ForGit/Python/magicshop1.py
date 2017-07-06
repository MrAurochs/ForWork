#Magic shop, the idea is that you have a magic shop and you buy and sell items
#you have a list of items which you can buy and sell
#Customers come in and offer to sell things to you at a certain price
# customers come in and offer to buy to you at a certain price.
# you must determine whether you want to buy/sell at the price.
# you also have to feed yourself each day to, so there is a certain pressure to sell

import random
import time

FOOD_PRICE = 5
STARTING_TIME = 480
STARTING_DAY = 0
STARTING_MONEY = 30

ITEM_DICT = {"mythril sword": 1870, "dragon tooth": 7 , "cap": 1 ,"iron helmet": 800, "broad axe": 1200 ,"wooden shield": 120,
             "club":5, "healing herbs": 11, "arrow": 17, "chain sickle": 550, "dragon egg": 27000
             , "copper sword": 30 , "eye of newt": 50, "rare tome": 3700, "talking bat": 270,
             "ring of invisibility": 5400, "potion of cure malaria": 350, "scale mail of lightning resistane": 2600,
             "emerald of demon taming": 12000, "Staff of Insect Command": 8000}

ITEM_LIST = list(ITEM_DICT.keys())

STARTING_INVENTORY = []

money = STARTING_MONEY
gametime = STARTING_TIME
day = STARTING_DAY



q = "You're a plucky young capitalist living in a world of wizards, there's lots of money to be made "
v = "buying and selling magic items to adventurers. Are you up to the challenge?"
message = q + v
def Display():

    hour = int((gametime/60) % 12)
    minute = gametime%60


    
    if len(inventory) < 1:
        print("inventory:" , ("time:" + str(hour) + ":"+ str(minute)).rjust(20), ("gold:" + str(format(money, ".2f"))).rjust(40) )
        print( ("day:" + str(day)).rjust(30))

    else:
        print("inventory:" , ("time:" + str(hour) + ":"+ str(minute)).rjust(20), ("gold:" + str(format(money, ".2f"))).rjust(40) )
        print(inventory[0], ("day:" + str(day)).rjust(30 - len(inventory[0])))
        for i in range(len(inventory)-1):
            print(inventory[i+1])
   

def Get_Customer():
    t = random.randint(1,3)
    if t ==1:
        print('you wait, but there is no customer')
    elif t == 2:
        
        item = random.choice(ITEM_LIST)
        item_price =  float(format(ITEM_DICT[item]  *  ((random.randint(0,100) -50)/100 + 1), '.2f'))
        
        if float(item_price) >= money:
            item = random.choice(["cap", "dragon tooth", "healing herbs", "arrow", "copper sword", "club"])
            item_price = float(format(ITEM_DICT[item]  *  ((random.randint(0,100) -50)/100 + 1), '.2f'))
            print("a customer walks in and would like to sell you an item")
            print("he has a " + item + ", and he would like to sell it to you for the price of " + str(item_price))
            Yes_No_Buy(item, item_price)
        else:
            print("a customer walks in and would like to sell you an item")
            print("he has a " + item + ", and he would like to sell it to you for the price of " + str(item_price))
            Yes_No_Buy(item, item_price)
    elif t == 3:
        
        if len(inventory) > 0: 
            item = random.choice(inventory)
            itemprice =  float(format(ITEM_DICT[item]  *  ((random.randint(0,100) -50)/100 + 1), '.2f'))
            print("a customer walks in and would like to buy your " + item + " for " + str(itemprice)+ " gold")
            Yes_No_Sell(item, itemprice)
        else:
            print("a customer comes in looking to buy goods, but you have nothing to sell")
    else:
        print("something is weird here....")
        pass 
       
def Yes_No_Sell(x, y):
    global inventory
    global money
    print("do you accept?")
    print("Enter Yes or No")
    Answer = input().lower()
    
    if len(Answer) == 0:
        print("yes or no please")
        Yes_No_Sell(x,y)
    
    elif Answer[0] == "y":
        inventory.remove(x)
        money += y
        print("The customer leaves with his newly purchased " + x)
    elif Answer[0] == "n":
        print("You just can't part with the " + x)
        print("the customer leaves")
    else:
        print("I'm sorry, I don't understand your answer")
        Yes_No_Sell(x, y)
        
def Yes_No_Buy(x, y):
    global inventory
    global money
    if float(y) > money:
        print("unfortunately, you can't afford the item")
        print("the customer leaves with his item")
        return
    print("Enter Yes or No")
    Answer = input().lower()

    if len(Answer) == 0:
        print("please entery yes or no")
        Yes_No_Buy(x,y)
        
    elif Answer[0] == "y":
            inventory.append(x)
            money -= y
            print("the customer leaves with his money")

    elif Answer[0] == "n":
            print("the customer leaves with his item")
    else:
            print("I don't understand your answer") 
            Yes_No_Buy(x,y )

    
    

def Win_Game():
    print("Congratulations, you have amassed enough wealth for your Airship.....you can now travel the world in style")
    print("would you like to play again?  Yes or No")
    Answer = input().lower()[0]
    if Answer == "n":
            import sys; sys.exit()
    elif Answer == "y":
        New_Game()
    else:
        print("I'm sorry, I don't understand....")
        Win_Game()

def Lose_Game():
    
    print ("would you like to play again? Yes or No")
    if Answer == "n":
            import sys; sys.exit()
    elif Answer == "y":
        New_Game()
    else:
        print("I'm sorry, I don't understand....")
        Lose_Game()
    

def Turn():
    global gametime
    global day
    global money
    Display()
    if money >= 300000:
                    Win_Game()
    Get_Customer()
    gametime += 30
    if gametime >= 1200:
            print("you feel really tired and hungry....time to eat dinner and get to bed")
            time.sleep(4)
            day += 1
            money -= FOOD_PRICE
            if money < 0:
                print("you have run out of money!!!!!,  you are now forced to sell the shop to feed yourself...")
                Lose_Game()
            else:
                pass
            gametime = 480
            print("you rise, early in the morning, ready to make money")
            Turn()
    else:
            pass
    
            
        
            


    
    

def New_Game():
    global gametime
    global money
    global inventory
    global day 
    money = STARTING_MONEY
    gametime = STARTING_TIME
    inventory = STARTING_INVENTORY
    day = STARTING_DAY

    print(message)

    while money > 0:
        Turn()

New_Game()
    

