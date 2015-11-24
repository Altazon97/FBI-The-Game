coordinates = [[[4, 5], [6, 7], [8, 9]], [[0, 1], [2, 13], [18, 32]]]

def isHit():
    """Figures out if the inputted coordinates has hit part of a bone.
    """
    for i in range(2):
        line = coordinates[i]
        for j in range(3):
            pos = line[j]
            if int(guess[0]) == pos[0] and int(guess[1]) == pos[1]:
                print("True")

guess = str(input())
guess = guess.split()
isHit()
