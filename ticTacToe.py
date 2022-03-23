import sys

# Method used to print and draw the board as the game is played.
# theBoard: Dictionary containing the current occupying player for each square
def displayBoard(theBoard):

    print('  |--------------------|')
    print('  |      |      |      |')
    print('3 |  '+ theBoard['a3'] +'   |   ' + theBoard['b3'] + '  |   ' + theBoard['c3'] + '  |')
    print('  |      |      |      |')
    print('  |------+------+------|')
    print('  |      |      |      |')
    print('2 |  '+ theBoard['a2'] +'   |   ' + theBoard['b2'] + '  |   ' + theBoard['c2'] + '  |')
    print('  |      |      |      |')
    print('  |------+------+------|')
    print('  |      |      |      |')
    print('1 |  '+ theBoard['a1'] +'   |   ' + theBoard['b1'] + '  |   ' + theBoard['c1'] + '  |')
    print('  |      |      |      |')
    print('  |--------------------|')
    print('     A       B     C   ')
    print()

# Method that takes the user inpute to verify it is a valid move or breaks the rules of the game.
# theBoard: Dictionary containing the current occupying player for each square
# player: variable indicating which players turn it is
def validMove(theBoard, player):

    valid = False

    while valid == False:
        print()
        playerMove = input('It is ' + player + '\'s turn. Please enter the coordinate for your turn.')

        if playerMove.lower() == 'quit' or playerMove.lower() == 'q' :
            sys.exit("Thank you for playing.")
        elif playerMove.lower() == 'a3' or playerMove.lower() == 'b3' or playerMove.lower() == 'c3' or playerMove.lower() == 'a2' or playerMove.lower() == 'b2'or playerMove.lower() == 'c2' or playerMove.lower() == 'a1' or playerMove.lower() == 'b1' or playerMove.lower() == 'c1':
            if theBoard[playerMove.lower()] != ' ':
                print('This space is already claimed. Please select a space that is currently not claimed')
            else:
                print('Player ' + player + ' has claimed the space ' + playerMove.upper() + '.')
                theBoard[playerMove.lower()] = player
                valid = True
        else:
            print('The coordinate entered does not match a space on the board. Please enter a valid space.')

    return theBoard

# Checks most recent move by the player to verify if the move has won the game or not
# theBoard: Dictionary containing the current occupying player for each square
# player: variable indicating which players turn it is
def checkWinner(theBoard, player):

    if theBoard['a3'] == theBoard['a2'] == theBoard['a1'] != ' ':
        return True
    elif theBoard['b3'] == theBoard['b2'] == theBoard['b1'] != ' ':
        return True
    elif theBoard['c3'] == theBoard['c2'] == theBoard['c1'] != ' ':
        return True
    elif theBoard['a3'] == theBoard['b3']  == theBoard['c3'] != ' ':
        return True
    elif theBoard['a2'] == theBoard['b2'] == theBoard['c2'] != ' ':
        return True
    elif theBoard['a1'] == theBoard['b1']  == theBoard['c1'] != ' ':
        return True
    elif theBoard['a1'] == theBoard['b2'] == theBoard['c3'] != ' ':
        return True
    elif theBoard['a3'] == theBoard['b2'] == theBoard['c1'] != ' ':
        return True
    else:
        return False
        
def ticTacToe():

    turn = 1
    player = 'X'
    winsX = 0
    winsO = 0
    numTies = 0
    theBoard = {'a3': ' ', 'b3': ' ', 'c3': ' ',
                'a2': ' ', 'b2': ' ', 'c2': ' ',
                'a1': ' ', 'b1': ' ', 'c1': ' '}

    displayBoard(theBoard)

    while turn < 10:
        turn = 1
        player = 'X'
        theBoard = {'a3': ' ', 'b3': ' ', 'c3': ' ',
                    'a2': ' ', 'b2': ' ', 'c2': ' ',
                    'a1': ' ', 'b1': ' ', 'c1': ' '}

        print('The board is broken down into coordinates such as \"A1, B2, C3\". Please enter move in this format to claim an unoccupied space on your turn.')
        print('At any point entering \"quit\" or \"q\" during the players move will close the session')
        
        for i in range(9):
            theBoard = validMove(theBoard, player)
            print()
            print('Turn ' + str(turn))
            displayBoard(theBoard)

            if turn >= 5:

                if checkWinner(theBoard, player) == True and player == 'X':
                    print('Player ' +player+ ' is the Winner.')
                    winsX += 1
                    print( 'Wins X : ' + str(winsX))
                    print( 'Wins O : ' + str(winsO))
                    print( 'Ties : ' + str(numTies))
                    print()
                    break
                elif checkWinner(theBoard, player) == True and player == 'O':
                    print('Player ' +player+ ' is the Winner.')
                    winsO += 1
                    print( 'Wins X : ' + str(winsX))
                    print( 'Wins O : ' + str(winsO))
                    print( 'Ties : ' + str(numTies))
                    print()
                    break
                elif checkWinner(theBoard, player) == False and turn == 9:
                    print('The round has ended in a Tie')
                    numTies += 1
                    print( 'Wins X : ' + str(winsX))
                    print( 'Wins O : ' + str(winsO))
                    print( 'Ties : ' + str(numTies))
                    print()
                    break 
            
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

            turn += 1
        
if __name__ == "__main__":
    ticTacToe()
