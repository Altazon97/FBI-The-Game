coordinates = [[[4, 5], [6, 7], [8, 9], [10, 12]], [[41, 5], [6, 7], [8, 9], [10, 11]], [[4, 5], [6, 7], [8, 9], [10, 100]]]

def isHit():
    """Figures out if the inputted coordinates has hit part of a bone.
    """
    for i in range(3):  #do the following for all the bones...
        line = coordinates[i]
        print (line)
        for j in range(4): #check if coordinate matches a particular bone
            pos = line[j]
            if int(guess[0]) == pos[0] and int(guess[1]) == pos[1]:
                print("****HIT!!!!****")
                return True

guess = str(input())
guess = guess.split()
isHit()
