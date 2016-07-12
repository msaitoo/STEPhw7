from random import randint
data = [{"Where":[3,3],"As":1},{"Where":[3,4],"As":1},{"Where":[3,5],"As":1},{"Where":[3,6],"As":1},{"Where":[3,7],"As":1}]

def point(x,y):
    point = 0
    if x == 1 and y ==1:
        point += 10
    if 

def nextmove(data):
    validmoves = []
    for i in range(len(data)):
        move = ""
        move += chr(ord('A') + int(data[i]["Where"][0]) - 1)
        move += str(data[i]["Where"][1])
        validmoves.append(move)
    choose = randint(0,len(data)-1)
    nextmove = validmoves[choose]
    return nextmove
    
nextmove(data)