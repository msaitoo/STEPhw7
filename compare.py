
def points(move):
    point = 0
    move = move["Where"]
    if move[0] == 2 or move[0] == 7:
        point -= 10
    elif move[0] == 1 or move[0] == 8:
        point += 5
    else:
        point += 1
    if move[1] == 2 or move[1] == 7:
        point -= 10
    elif move[1] == 1 or move[1] == 8:
        point += 5
    else:
        point += 1
    return point



def rearrange(moves, minmax):
    new_moves = []
    point = []
    if len(moves) > 4:
        for i in moves:
            point.append(points(i))
        print point
        while len(new_moves) < 4:
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

data = [{"Where":[4,3],"As":1},{"Where":[3,4],"As":1},{"Where":[6,5],"As":1},{"Where":[5,6],"As":1},{"Where":[1,2],"As":1}]