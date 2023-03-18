import math
from plane import Plane


def botMove(gamePlane):
    bestScore = -math.inf
    bestMove = ()
    for i in range(1, gamePlane.length+1):
        for j in range(1, gamePlane.length+1):
            if gamePlane.cellIsEmpty(i, j):
                gamePlane.markCell(i, j, 'bot')
                score = minMax(gamePlane, False)
                gamePlane.clearCell(i, j)
                if(score > bestScore):
                    bestMove = (i, j)
                    bestScore = score
    return bestMove


def minMax(gamePlane, botTurn):

    win = gamePlane.isComplete()

    if win != None:
        return mapState(win)

    if botTurn:
        bestScore = -math.inf
        for i in range(1, gamePlane.length+1):
            for j in range(1, gamePlane.length+1):
                if gamePlane.cellIsEmpty(i, j):
                    gamePlane.markCell(i, j, 'bot')
                    score = minMax(gamePlane, False)
                    gamePlane.clearCell(i, j)
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(1, gamePlane.length+1):
            for j in range(1, gamePlane.length+1):
                if gamePlane.cellIsEmpty(i, j):
                    gamePlane.markCell(i, j, 'user')
                    score = minMax(gamePlane, True)
                    gamePlane.clearCell(i, j)
                    bestScore = min(score, bestScore)
        return bestScore


def mapState(win):
    if win == True:
        return 10
    if win == False:
        return -10
    return 0


def checkIfWin(gamePlane):
    win = gamePlane.isComplete()
    if(win == "DRAW"):
        raise Exception('It is a draw!')
    if(win != None):
        raise Exception('Match Ends\n'+('You won' if(not win) else 'bot won'))


level = int(input('which level do you want to play?\n'))
gamePlane = Plane(level)
while True:
    inp = input('type \'end\' to exit\nYour move: \n\'row\' \'col\'\n')
    if(inp == 'end'):
        print("you exited the game")
        break

    try:
        x, y = map(int, inp.split())
    except:
        if inp == 'end':
            break

    try:
        gamePlane.markCell(x, y, "user")
        gamePlane.printInstance()
        print()
    except Exception as e:
        print(e)
        continue

    try:
        checkIfWin(gamePlane)
    except Exception as e:
        print(e)
        break

    x, y = botMove(gamePlane)
    gamePlane.markCell(x, y, 'bot')
    gamePlane.printInstance()
    try:
        checkIfWin(gamePlane)
    except Exception as e:
        print(e)
        break
    finally:
        print()
