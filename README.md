Written based on code provided by https://github.com/step16/hw7

Edited 'pickMove' function:
Considers following
1) number of valid moves
2) give points (positive or negative) to important squares

jibun=[] and aite=[] stores numbers of valid moves for this round and the round after.

rearrange() rearranges given valid moves into order of importance, to narrow down the number of possibilities to consider to reply quickly.

流れ：
1) Considers valid moves I can take and narrows it down using rearrange()
2) For each of those valid moves, simulate the board after that particular move and considers the number of valid moves of the opponent at that round.
3) Narrows down possible opponent's moves and simulate the board after each oppoenent's moves.
4) Considers possible my round after opponent's move. Again, consideres the number of valid moves and stores that number.

5) When number of valid moves for opponent's and my round (after opponent's move) fore each 'current' possible moves are stored,
add points for when number of aite's move is 0
reduce points for the numbers of valid moves the opponent could have
reduce points for number of my move = 0
add points for the amount of possible moves I could have

6) Evaluate 'current' valid moves to see if any of them are located at squares which would be a disadvantage.
7) Choose the one with most points and return.