# a program that controls a lunar rover 
# by Ayesha Bhutto 

import random # imports random numbers

x = 0 # a variable that sets x to equal 0
y = 0 # a variable that sets y to equal 0 

print ("Welcome to the Luner Rover! Let's see what adventures you go on today...") # print statement addressing the introduction to the game 


running = True # the program will repeat itself as long as it is running 

while running: # the program loops here 
    print ("\nThe rover is at (%i,%i)." %(x,y)) # a print statement issuing where the lunar rover is 
    
    position = input("Please enter the position: ") # user inputs the commannd with direction and coordinate 
    

    space = position.find(" ") # variable that finds the space between the command 
    
    if space != -1: # space cannot equal a negative number so the direction is set to be anything before that
        direction = position[:space] # direction is anything before the space 
 
    else:           # if the space does equal a negative, then the direction equals directly to the position 
        direction = position 
    
   
     
    if direction == "north":    # if statement about the direction being north 
        coordinate = int(position[space:]) # the number after the space in the command is turned into an integer 
        y += coordinate # since y is 0 at the moment, it will add whatever the integer is to make the lunar rover "move" 
        
    elif direction == "south":  # if statement about the driection being south
        coordinate = int(position[space:]) # the number after the space in the command is turned into an integer
        y -= coordinate # since y is 0 at the moment, y will subtract whatever number is given since the direction is south 
        
    elif direction == "east":   # if statement about the direction going east
        coordinate = int(position[space:]) # the number after the space is defined as an integer
        x += coordinate # x is 0 at the moment but this will add to the x coordinate since the direction is going east
        
    elif direction == "west":   # if staement about the direction going west
        coordinate = int(position[space:]) # the number after the space is defined as an integer
        x -= coordinate  # since x is 0, x will subtract with the given value since the direction is going west

    elif direction == "dig":    # user is finding an object on the mooon 
        object = random.choice(["a special moon rock","a spider","an apple", "my report card", "an orange"]) # program uses a random object to be found each time  
        print ("Oh look! You have found %s. That's not relevant anyway." %object) # print statement issuing what has been found 
        
    elif direction == "reset":  # resets the program to go back to the beginning which is (0,0)
        x = 0 # x is set to be 0
        y = 0 # y is set to be 0
        print ("The rover has been reset to (%i,%i)." %(x,y))    # a print statement issuing the rover has been reset
        
        
    elif direction == "rest":   # if user enters rest, the program breaks 
        break 
    
        
        
    elif direction == "moveto": # the direction is defined if the position is moveto, which is the lunar rover moving to a certain area 
        space = space+1 # space is created by addding one more space to it
        command = position[space:] # anything after the first space is the first movement
        secondspace = command.find(" ") # after the command creates the second space between the moveto and integers
        xpoint = int[:secondspace] # turns anything before the secondspace to an integer
        ypoint = int[secondspace:] # turns anything after the second space to an integer
        print ("You have moved the rover to (%i,%i)," %(xpoint,ypoint)) # print statement issuing what the movement is 
              
        
        
    else:   # if user enters anything else rather than a valid direction, the program will appear as invalid and continue to ask until the command is inputted properly 
        print("Error, this move cannot be made. Enter the direction and then your point (ex.north 4): ")    
    

    
   
    
        
    
        
    
