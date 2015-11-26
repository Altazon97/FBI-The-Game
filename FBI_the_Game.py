"""
FBI_the_Game.py

Eric Sund
Andy Zeng

November 25, 2015

This program allows a user to guess the locations of bones that Sherlock Holmes
buried for his dog in a custom-sized grid.  Bones can face either vertical or
horizontal.
"""


#=============================== Start Defining Functions ===============================#

#Get the data file
def getDataFile():
    """This function asks the user to enter the name of the data file and reads it.
    If it cant be read or doesn't exist, the user is asked to try again.
    """

    #Open the file before doing anything
    getfile = 0
    while getfile == 0:
        dataFile = input("Please, enter the name the data file: ")
        try:
            data = open(dataFile, 'r')
            getfile = 1
        except ValueError:
            print("\nYou have entered an incorrect filename, please try again.\n")
    return data


#Get the coordinates of the bones
def getCoordinates():
    """This function gets the coordinates of bones from data file.
    """

    eachLine = data.readlines()
    allCoordinates = []
    #Iterate through lines
    for currentLine in range(len(eachLine)):
        line = eachLine[currentLine].split()
        i = 0
        #Record the coordinate values
        while i < len(line):
            allCoordinates.append(line[i:i+2])
            i += 2
    #Group coordinates into bones and make a 3D list
    bonelist = []
    for i in range(numberOfBones):
        bonelist.append(allCoordinates[sizeOfBone*i : sizeOfBone*(i+1)])
    return bonelist


#Check to see if user guessed coordinates are a hit
def isHit():
    """This function returns True if the inputed coordinates has hit part of a bone.
    """

    for i in range(numberOfBones):  #Do the following for all the bones...
        line = bonelist[i]
        for j in range(sizeOfBone): #Check if coordinate matches a particular bone
            pos = line[j]
            if int(guess[0]) == int(pos[0]) and int(guess[1]) == int(pos[1]):
                print("\n****HIT!!!!****")
                return True


#Check if user has dug up an entire bone
def isCompleteBone(row, col):
    """This function takes a coordinate and checks its surroundings ((sizeOfBone - 1) positions in all four directions)
    for positions where the user has revealed "B". It then looks within all these positions to see whether the user has fully revealed a bone
    """

    position = [row,col]            #initialize your position with your last guest
    coordinate_list = [position]    #list of all coordinates within (sizeOfBone - 1) of your selected position, starts with your position
    hit_list = []                   #list of all coordinates that contain "B" within coordinate_list
    new_hit_list = []               #list of all coordinates within hit_list that match a specific bone
    bone = []

    #Save all coordinates (sizeOfBone - 1) above your selected position
    for i in range(sizeOfBone):
        position = [row - i, col]
        if position[0] != row and position[0] >= 0:     #if not your position and is within boundaries
            coordinate_list.append(position)
    #Save all coordinates (sizeOfBone - 1) below your selected position
    for i in range(sizeOfBone):
        position = [row + i, col]
        if position[0] != row and position[0] < xAxis:  #if not your position and is within boundaries
            coordinate_list.append(position)
    #Save all coordinates (sizeOfBone - 1) left of your selected position
    for i in range(sizeOfBone):
        position = [row, col - i]
        if position[1] != col and position[1] >= 0:     #if not your position and is within boundaries
            coordinate_list.append(position)
    #Save all coordinates (sizeOfBone - 1) right of your selected position
    for i in range(sizeOfBone):
        position = [row, col + i]
        if position[1] != col and position[1] < yAxis:  #if not your position and is within boundaries
            coordinate_list.append(position)

    #Create hit_list with only valid hits from coordinate_list
    for pos in coordinate_list:
        if yard[pos[0]][pos[1]] == "B":
            hit_list.append(pos)
    #Iterate through each bone from your data
    for i in range(numberOfBones):
        #Change the bone coordinates from strings to integers
        for pos in bonelist[i]:
            pos = [int(pos[0]),int(pos[1])]
            bone.append(pos)
        #Take all positions from hit_list that are found in current bone and make new_hit_list
        for pos in hit_list:
            if pos in bone:
                new_hit_list.append(pos)

        #Sort and compare bone and new_hit_list to see if they are equivalent
        if sorted(bone)== sorted(new_hit_list):
            print("\nYou have fully uncovered bone " + str(i) + ". Great Job!")

        #Clear bone and new_hit_list to iterate through next bone
        bone = []
        new_hit_list = []


#Check to see if user has revealed all bones
def isCompleteYard():
    """This function generates a yard with all of the bones displayed, compares it to the user-generated yard.
    If the two are the same (i.e. user is done the game), prints out the yard and returns True.
    """

    #Create complete yard to compare
    complete_yard = [["." for x in range(int(xAxis))] for x in range(int(yAxis))]   #new matrix for the complete yard
    for i in range(numberOfBones):  #Do the following for all the bones...
        line = bonelist[i]
        for j in range(sizeOfBone): #Check if coordinate matches a particular bone
            pos = line[j]
            row = int(pos[0])
            col = int(pos[1])
            #Assign each B to complete yard
            complete_yard[row][col] = "B"

    #Check if user yard is complete
    if yard == complete_yard:
        print("\n")         #Separator for aesthetic effect
        showYard()          #Display completed yard
        return 1


#Reveal the bone if user guess correctly
def revealBone():
    """This function changes a "." to a "B" in the yard matrix when a bone is hit.
    """

    if isHit():
        #Replace the "." with "B"
        yard[int(guess[0])][int(guess[1])] = "B"
        #Check if the user has dug up an entire bone
        isCompleteBone(int(guess[0]),int(guess[1]))
    else:
        print("\n****OOPS! MISSED!****")


#Display the yard
def showYard():
    """This function prints the yard with all of the bones uncovered by the user so far.
    """

    top = "" #x axis numbers
    sideNum = 0 #y axis numbers
    #Create the x axis numbers
    for i in range(xAxis):
        if i <= 9:
            top += str(i) + "  " #add one space between double digits
        if i > 9:
            top += str(i) + " "  #add two spaces between single digits
    print(top)
    #Create the rows of dots and stick the y axis numbers on the ends of them
    for row in yard:
        print("  ".join(row) + "  " + str(sideNum))
        sideNum += 1


#Check if input is an integer
def isNotInteger():
    """This function checks to see whether the input is an integer or not.
    """

    try:
        guess[0] = int(guess[0])
    except ValueError:
        return True


#=============================== End Defining Functions ===============================#


#================================= Start Main Program =================================#


#Introduce the User
print("""Welcome to Fast Bone Investigation (FBI) the game.
In this game, we dig out bones from Mrs. Hudson's backyard!""")

#Get the data file
data = getDataFile()

#Grab the dimensions from the data file to create the yard
gridInfo = data.readline()
gridInfo = gridInfo.split()
xAxis = int(gridInfo[0])
yAxis = int(gridInfo[1])
yard = [["." for x in range(int(xAxis))] for x in range(int(yAxis))] #matrix for the yard

#Grab the rest of the info on this line
numberOfBones = int(gridInfo[2])
sizeOfBone = int(gridInfo[3])

#Get the bone coordinates
bonelist = getCoordinates()

#Get the valid input with guardian code
running = True
while running:
    print("\nThere are " + str(numberOfBones) + " bones, each are " + str(sizeOfBone) + " cells long, buried in this backyard! Can you find them? ")
    showYard()
    guess = input("""To do so, please, enter the row and the column number of a cell in which you suspect a bone is buried
(e.g., 0 3 if you suspect that part of a bone is buried on the first row at the 4th column).
Enter -1 to quit : """).split()

    #Check for empty input
    if len(guess) == 0:
        print("***You have not entered anything. You need to enter a valid row and the column number!")
    #Check to ensure input is integer
    elif isNotInteger():
        print("***You have entered " + str(guess[0]) + ". You need to enter a valid row and the column number!")
    #If the user wishes to exit the game
    elif int(guess[0]) == -1:
        print("\nWasn't it fun! Bye!")
        running = False
    #If the user doesn't enter both row and column values
    elif len(guess) == 1:
        print("***You have entered only 1 value. You need to enter a valid row and the column number!")
    #If coordinate is beyond the backyard's dimensions
    elif (int(guess[0]) > int(yAxis) or int(guess[0]) < 0) or (int(guess[0]) > xAxis or int(guess[0]) < 0) or (int(guess[1]) > int(yAxis) or int(guess[1]) < 0) or (int(guess[1]) > xAxis or int(guess[1]) < 0):
        print("You needed to enter a row and column number of a cell that is within the backyard!")
    #Good to go!
    else:
        #See if user guess was correct
        revealBone()
        #If they have completed the game
        if isCompleteYard():
            print("\nCongratulations! You have found all the bones. Goodbye!\n")
            running = False


#================================== End Main Program ==================================#
