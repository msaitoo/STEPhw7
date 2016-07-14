
def givepoints(move):
    "Distribute points according to their locations"
    point = 0
    move = move["Where"]
    if move[0] == 2 or move[0] == 7:
        point -= 5
    elif move[0] == 1 or move[0] == 8:
        point += 5
    if move[1] == 2 or move[1] == 7:
        point -= 5
    elif move[1] == 1 or move[1] == 8:
        point += 5
    return point

def rearrange(moves, minmax):
    "Narrow down choices by choosing ones with higher/lower points"
    new_moves = []
    point = []
    if len(moves) > 5:
        for i in moves:
            point.append(givepoints(i))
        #print point
        while len(new_moves) < 5:
            if minmax == "max":
                index = point.index(max(point))
            if minmax == "min":
                index = point.index(min(point))
            new_moves.append(moves[index])
            moves.pop(index)
            point.pop(index)
    else:
        new_moves = moves
    return new_moves