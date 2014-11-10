""" Perfect tic-tac-toe """
""" by Dan Garcia       """
""" ...lots of values hardcoded, this was a quick-n-dirty API example """

import urllib.request

movetoindex = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}

def urlify(board):
    """Return a string with spaces ' ' replaces by '%20', required for URLs"""
    return(board.replace(" ","%20"))

def getmovesfromoracle(board):
    """Return the movelist for a Tic-Tac-Toe move"""
    return(eval(urllib.request.urlopen("http://nyc.cs.berkeley.edu:8080/gcweb/service/gamesman/puzzles/ttt/getNextMoveValues;board=" + urlify(board) + ";width=3;height=3;pieces=3").read().decode())['response'])

def prettyprint(board):
    """Pretty-print the tic-tac-toe board (no return value)"""
    print("")
    for row in range(3,0,-1):
        print("" + str(row) + " |" + board[(row-1)*3:(row)*3].replace(""," "))
    print("  +------")
    print("    A B C")

def domove(board, move):
    """Given a board (length 9 string of Xs and Os) and move {A1, B3, etc}, return an updated board"""
    for m in getmovesfromoracle(board):
        if m['move'] == move:
            return(m['board'])
    return(None)

def getmovevalues(moves):
    """Given the oracle-generated moves, Return a 'movevalues' board (length 9 string of {W=win,L=lose,T=tie} in each open slot)"""
    values = " " * 9
    for move in moves:
        index = movetoindex[move['move']]
        values = values[0:index] + move['value'][0].upper() + values[index+1:10]
    return values

def availablemoves(moves):
    """Given the oracle-generated moves, return a list of the available moves"""
    useravailablemoves = []
    for move in moves:
        useravailablemoves.append(move['move'])
    return(useravailablemoves)

def playttt():
    """Play the game of Tic-tac-toe and show the values of each move when requested"""
    board = " " * 9
    print("Welcome to Tic-Tac-Toe, brought to you by GamesCrafters!\n")
    print("We've 'solved' the game, so you can see the value (win, lose, tie)")
    print("of moves to make. Just type V whenever you want to see the values.")
    prettyprint(board)
    moves = getmovesfromoracle(board)
    while(moves):
        move = input("\nChoose your move (e.g., A1, B3, etc), V for values, Q for quit: ").upper()
        if (move == "Q"):
            break
        elif (move == "U"):
            print("http://nyc.cs.berkeley.edu:8080/gcweb/service/gamesman/puzzles/ttt/getNextMoveValues;board=" + urlify(board) + ";width=3;height=3;pieces=3")
        elif (move == "V"):
            print("\nHere are the values for this position's moves (W=win, T=tie, L=lose)")
            prettyprint(getmovevalues(moves))
        elif (move not in availablemoves(moves)):
            print("\nPlease choose V or one of (without quotes): " + str(availablemoves(moves)))
        else:
            board = domove(board, move)
            moves = getmovesfromoracle(board)
            prettyprint(board)
    print("Thanks for the game!")

if __name__ == '__main__':
    playttt()
