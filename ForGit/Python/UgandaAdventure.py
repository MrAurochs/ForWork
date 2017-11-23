import time
def End_Game():
    import sys; sys.exit()

Money = 50000

print ("""
You are in a compound in Uganda. It's made of concrete, brick with iron doors.
There is trash littered randomly on the ground mixed with the mud.
Half-naked children play around casually as their mothers cook or wash clothes.
A man comes up to you with outstretched and says "Umba Esente Mizungu.

What do you do?

""")

print("1 give him some money ")
print("2 ignore him and go to the market" )

one = input('> ')

if int(one[0]) == 1:

    Money -= 500
    print("You give him some money and decide that you want to got to the market")

elif int(one[0]) == 2:
    print("The man looks disappointed but you feel as if you made the right decision./n You head off to the market")
          
else:
    print("From out of nowhere a large man with a panga comes up to you and slashes your arm off")
    time.sleep(3)
    End_Game()


print("""
Wughaenda om marketar. You go to the market; on your journey you pass many goats
and a herd of cows.  Boda-boda's pass you by and people scream at you /'Hello my friend.
Hello my friend/' You wind your way through several dilapadated streets til finally you
come to the market.  The market is thronged with people selling things on mats.
You remember that your wife wanted a pineapple.

What do you do? 

""")

print ("1 get a pineapple")
print ("2 get a watermelon")
print ("3 get Irish Potatoes and Gnuts")

two = input('> ')

if int(two[0]) == 1:
          Money -= 1500
          print ("You're wife is going to be really happy. She loves Pineapple.")
          food = "pineapple"
elif int(two[0]) == 2:
          Money -= 3000
          food = "watermelon"
          print("You get yourself a hefty watermelon and decide to go home; you love watermelon")
        
elif int(two[0]) == 3:
          Money -= 4000
          food = "irish potatoes and gnuts"
          print("the gnuts look suspiciously like peanuts to you.... This should make a hearty meal, you decide to go home")
else:
          print("From out of nowhere a large man with a panga comes up to you and slashes your arm off")
          time.sleep(3)

          End_Game()


print("""
You decide to go home.
Do you want to take a Boda-Boda?
1. Yes
2. No

""")

three = input('> ')

if int(three[0]) == 1:
          Money -= 1000
          print ("you get on the boda-boda and soar off to home. Unfortunately you did not count on the driver being drunk")
          print("He goes to fast and hits a crevice in the poorly maintained road. As you are flying in the air you think to yourself:\nWell this is dumb")
          print("That's the last thought you have because you have because your brain ends up splattered on the pavement")
          time.sleep(3)
          End_Game()

elif int(three[0]) == 2:
          print("you decide erienda amawolu, to go by your feet, is the best choice")

else:
    print("From out of nowhere a large man with a panga comes up to you and slashes your arm off")
    time.sleep(3) 
    End_Game()


if food == "pineapple":
          print(""" You return home to find your wife wating for you she is ecstatic that you brought her a pineapple.
            /'I love you dear,/' she says with a laugh. 
            """)
else:
          print("""Your wife is quite upset with you, because she REALLY wanted pineapple. You end up going out and getting her another one.

            """)
          Money -= 1500

print(""" This concludes your day, you sit down to your computer to play some Zork.
You feel quite happy with yourself. You're really glad you didn't die.""" )

time.sleep(3)
End_Game()
