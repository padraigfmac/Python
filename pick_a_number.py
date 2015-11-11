"""
Programmer: Padraig Mac Donnchadha
Date: December 2014
Pick a number.
Each player in turn removes the number either at the beginning or the end of a list of numbers. 
When all the numbers have been removed, each player sums up the numbers they chose. The player with the highest total is the winner.
"""


# Global Variable
player = 1

# Dictionary
SCOREINDEX = {1:0, -1:1}

def pick_a_number(board):
    """
    Recursive function using minimax variant.
    Takes a list of numbers representing the game board.
    Returns a tuple that is the score of the game if both players play optimally.
    The returned tuple should be ordered with the current player's score first and the other player's score second
    """
    global player
    cur_player = int(player)
    #print player, board

    
    # base case, only 2 numbers left
    if len(board) == 2:
        #print "+++++"
        if board[0]*cur_player > board[1]*player:
            rtn_score = (board[0], board[1])
        else:
            rtn_score = (board[1], board[0])
        #print rtn_score
        return rtn_score

    # Update the player
    player = cur_player *(-1)
    
    #print "-----"

    #print board

    # option 1 take the first number, this is score1
    new_board = list(board)
    #print board
    num = new_board.pop(0)
    #print cur_player, num, new_board
    score = pick_a_number(new_board)
    #print cur_player, num, score
    if cur_player == 1:
        score1 = (score[0] + num, score[1])
    else:
        score1 = (score[0], score[1] + num)
    dif1 = (score1[0] - score1[1]) * cur_player
    #print cur_player, num, score, score1, dif1
    
    # Update the player
    player = cur_player *(-1)
    
    # option 2 take the second number, this is score2
    new_board = list(board)
    num = new_board.pop(-1)
    #print cur_player, num, new_board
    score = pick_a_number(new_board)
    #print cur_player, num, score
    if cur_player == 1:
        score2 = (score[0] + num, score[1])
    else:
        score2 = (score[0], score[1] + num)
    dif2 = (score2[0] - score2[1]) * cur_player
    #print cur_player, num, score, score2, dif2

    # if dif1 < dif2, rtn_score is score1, else it's score2
    if dif1 > dif2:
        rtn_score = score1
    else:
        rtn_score = score2
    #print "rtn_score:", rtn_score
    return rtn_score

testboard = [3, 5, 2, 1]
#testboard = [6, 3, 9, 7, 1]
#testboard = [12, 9, 7, 3, 4, 7, 4, 7, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1]
print pick_a_number(testboard)

