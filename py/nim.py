# nim
# Jihae Park
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

# starting with a bag of 12 stones
stones = 12


# Scanner for our user input
 
print("*****************")
print("Welcome to Nim!")
print("*****************")

       
# loop until game ends
while stones > 0:
   
    #ask the user input for the number of stones to be taken away
    print("There are " + str(stones) + " stones in our bag.")
    stonesTaken = int(input("How many would you like to choose? 1, 2, or 3."))
    
    #when the user tries to take less than 1 or greater than 3, this will happen
    if (stonesTaken > 3) or (stonesTaken < 1):  
        print("Ooops, that's not a valid number of stones to take!")
        stonesTaken = int(input("Try again."))
    
    print("You chose to take " + str(stonesTaken))

    stones -= stonesTaken

    if stones == 0:
        print("YOU WIN!")
        break
    else:
        print("There are now " + str(stones) + " stones in the bag.\n It's now the AI's turn.") 
    
    
    
   

    # AI's turn - GOAL: WIN!
    stonesTaken = 4 - stonesTaken
    print("The computer chose to take " + str(stonesTaken))
    stones -= stonesTaken
    
    if stones == 0:
        print("AI WINS! SORRY. :(((")
        break
    else:
      print("There are now " + str(stones) + " stones in the bag.\n It's now your turn.")
    

    




# check for win

# AI turn

# check win


