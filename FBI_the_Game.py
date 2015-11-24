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

#import modules
import re, random

#grab the dimensions from the data file to create the yard
gridInfo = data.readline()
gridInfo = gridInfo.split()
xAxis = gridInfo[0]
yAxis = gridInfo[1]
yard = [["." for x in range(int(xAxis))] for x in range(int(yAxis))] #matrix for the yard

#grab the rest of the info on this line
numberOfBones = gridInfo[2]
sizeOfBone = gridInfo[3]

#define all the functions
def getCoordinates():
    """Gets the coordinates of bones from FBI_the_Game_Data_2.txt
    """
    allCoordinates = []
    coordinates = []
    eachLine = data.readlines()
    currentLine = 1
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
    Otherwise, False is returned if part of a bone is not hit.
    """
    for i in range(numberOfBones):  #do the following for all the bones...
        line = coordinates[i]
        for j in range(sizeOfBone): #check if coordinate matches a particular bone
            pos = line[j]
            if int(guess[0]) == pos[0] and int(guess[1]) == pos[1]:
                return True
            else:
                return False

def changeBonePart():
    """
    This function changes a "." to a "B" in the yard matrix when a bone is hit.
    """
    if isHit():
        yard[guess[0]][guess[1]] = "B"

def showYard():
    """
    This function shows either the entire yard with all the locations of the buried bones
    which are randomly determined, or shows the yard with one soecified bone by changing
    the desiredYard parameter.
    """

    top = "" #x axis numbers
    sideNum = 0 #y axis numbers
    #create the x axis numbers
    for i in range(int(xAxis)):
        if i <= 9:
            top += str(i) + "  " #add one space between double digits
        if i > 9:
            top += str(i) + " "  #add two spaces between single digits
    print(top)
    #create the rows of dots and stick the y axis numbers on the ends of them
    for row in yard:
        print("  ".join(row) + "  " + str(sideNum))
        sideNum += 1

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
    print("\n\nThere are " + numberOfBones + " bones, each are " + sizeOfBone + " cells long, buried in this backyard! Can you find them? ")
    showYard()
    choice = input("""To do so, please, enter the row and the column number of a cell in which you suspect a bone is buried
(e.g., 0 3 if you suspect that part of a bone is buried on the first row at the 4th column).
Enter -1 to quit : """)

    getCoordinates()
    choice = choice.split()

    if len(choice) == 0:
        print("***You have not entered anything. You need to enter a valid row and the column number!")
    elif int(choice[0]) == -1:
        print("\nWasn't it fun! Bye!")
        running = False
    elif len(re.findall("[A-Z]", choice)) >= 1 or len(re.findall("[a-z]", choice)) >= 1:
        print("***You have entered " + str(guess) + ". You need to enter a valid row and the column number!")
    elif re.match("^\d+?\.\d+?$", choice) is not None:  #checking for floats
        print("***You have entered " + str(choice) + ".  That doesn't make sense.  Please enter an integer.")
    elif len(choice) == 1:
        print("***You have entered only 1 value. You need to enter a valid row and the column number!")
    elif (choice[0] > yAxis or choice[0] < yAxis) or (choice[0] > xAxis or choice[0] < xAxis):
        print("You needed to enter a row and column number of a cell that is within the backyard!")
        running = False
    elif int(choice) < -1 or int(choice) > 8:
        print("***You have entered " + str(choice) + " which is not in the desired range. You need to enter a valid number!")
    else:
        #good to go!
        changeBonePart()
        showYard()
