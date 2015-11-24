"""
FBI.py

Eric P. Sund
November 4, 2015

This program allows a user to guess the locations of bones that Sherlock Holmes
buried for his dog in a custom-sized grid.  Bones can face either vertical or
horizontal.
"""

#open the file before doing anything
dataFile = "FBI_the_Game_Data_2.txt"
data = open(dataFile, 'r')

#instance variables
coordinates = []

#grab the dimensions from the data file to create the yard
gridInfo = data.readline()
gridInfo = gridInfo.split()
xAxis = int(gridInfo[0])
yAxis = int(gridInfo[1])
yard = [["." for x in range(int(xAxis))] for x in range(int(yAxis))] #matrix for the yard

#grab the rest of the info on this line
numberOfBones = int(gridInfo[2])
sizeOfBone = int(gridInfo[3])

#define all the functions
def getCoordinates():
    """Gets the coordinates of bones from FBI_the_Game_Data_2.txt
    """
    allCoordinates = []
    eachLine = data.readlines()
    currentLine = 0
    while currentLine < len(eachLine):
        line = eachLine[currentLine].split()
        i = 0
        while i <= len(line):
            allCoordinates.append(line[i:i+2])
            i += 2
        allCoordinates.pop(-1) #get rid of last single element
        currentLine += 1
    #organize into 3D list
    coordinates.append(allCoordinates[0:4])
    coordinates.append(allCoordinates[4:8])
    coordinates.append(allCoordinates[8:12])
    coordinates.append(allCoordinates[12:16])

def isHit():
    """
    Returns True if the inputted coordinates has hit part of a bone.
    """
    for i in range(numberOfBones):  #do the following for all the bones...
        line = coordinates[i]
        for j in range(sizeOfBone): #check if coordinate matches a particular bone
            pos = line[j]
            if int(guess[0]) == int(pos[0]) and int(guess[1]) == int(pos[1]):
                print("****HIT!!!!****")
                return True

def changeBonePart():
    """
    This function changes a "." to a "B" in the yard matrix when a bone is hit.
    """
    if isHit():
        yard[int(guess[0])][int(guess[1])] = "B"
    else:
        print("****OOPS! MISSED!****")

def showYard():
    """
    This function shows either the entire yard with all the locations of the buried bones
    which are randomly determined, or shows the yard with one soecified bone by changing
    the desiredYard parameter.
    """

    top = "" #x axis numbers
    sideNum = 0 #y axis numbers
    #create the x axis numbers
    for i in range(xAxis):
        if i <= 9:
            top += str(i) + "  " #add one space between double digits
        if i > 9:
            top += str(i) + " "  #add two spaces between single digits
    print(top)
    #create the rows of dots and stick the y axis numbers on the ends of them
    for row in yard:
        print("  ".join(row) + "  " + str(sideNum))
        sideNum += 1

def isNotInteger():
    try:
        guess[0] = int(guess[0])
    except ValueError:
        return True

"""
def showBone(boneNumber):
    #showBone() changes a "." to a "B" when a bone is hit.

    if

    #draw the bones
    yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
    if bones[boneNumber-1][2] == 'right':
        for i in range(6):
            yardToShowBoneIn[bones[(boneNumber-1)][0]][bones[(boneNumber-1)][1] + i] = "B"

    elif bones[boneNumber-1][2] == 'left':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6, 0, -1):
            yardToShowBoneIn[bones[(boneNumber-1)][0]][bones[(boneNumber-1)][1] - i] = "B"

    elif bones[boneNumber-1][2] == 'up':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6, 0, -1):
            yardToShowBoneIn[bones[(boneNumber-1)][0] - i][bones[(boneNumber-1)][1]] = "B"

    elif bones[boneNumber-1][2] == 'down':
        yardToShowBoneIn = [["." for x in range(15)] for x in range(12)]
        for i in range(6):
            yardToShowBoneIn[bones[(boneNumber-1)][0] + i][bones[(boneNumber-1)][1]] = "B"

    print("\nHere is the backyard with 1 bone buried: ")
    showYard(yardToShowBoneIn)
"""

#MAIN
print("""Welcome to Fast Bone Investigation (FBI) the game.
In this game, we dig out bones from Mrs. Hudson's backyard!""")

#get the valid input with guardian code
running = True
while running:
    print("\n\nThere are " + str(numberOfBones) + " bones, each are " + str(sizeOfBone) + " cells long, buried in this backyard! Can you find them? ")
    showYard()
    guess = input("""To do so, please, enter the row and the column number of a cell in which you suspect a bone is buried
(e.g., 0 3 if you suspect that part of a bone is buried on the first row at the 4th column).
Enter -1 to quit : """)

    getCoordinates()
    guess = guess.split()

    if len(guess) == 0:
        print("***You have not entered anything. You need to enter a valid row and the column number!")
    elif int(guess[0]) == -1:
        print("\nWasn't it fun! Bye!")
        running = False
    elif isNotInteger():
        print("***You have entered " + str(guess[0]) + ". You need to enter a valid row and the column number!")
    elif len(guess) == 1:
        print("***You have entered only 1 value. You need to enter a valid row and the column number!")
    elif (int(guess[0]) > int(yAxis) or int(guess[0]) < 0) or (int(guess[0]) > xAxis or int(guess[0]) < 0) or (int(guess[1]) > int(yAxis) or int(guess[1]) < 0) or (int(guess[1]) > xAxis or int(guess[1]) < 0):
        print("You needed to enter a row and column number of a cell that is within the backyard!")
    else:
        #good to go!
        changeBonePart()
