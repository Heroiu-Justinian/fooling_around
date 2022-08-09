from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("""+-------+-------+-------+
|       |       |       |""")
    print(f"|    {board[0][0]}  |   {board[0][1]}   |   {board[0][2]}   |")
    print("""|       |       |       |
+-------+-------+-------+
|       |       |       |""")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("""|       |       |       |
+-------+-------+-------+
|       |       |       |""")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("""|       |       |       |
+-------+-------+-------+""")

    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            choice = int(input('Enter your move'))
            x ,y = (choice - 1) // 3, (choice-1)%3 
            if board[x][y].isdigit():
                    board[x][y] = "O"
                    break
            else:
                print("This square is occupied")
        except:
            print("the provided input is illegal")
            continue
                
       

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    available = []
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit():
                available.append((int(i),int(j)))
    return available


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winset = {
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
    }
    
    played = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                played.add((i,j))
    #print(played)
    for win in winset:
        if len(played.intersection(win)) == 3: 
            return True
    return False
        
    


def draw_move(board):
    available = make_list_of_free_fields(board)
    x,y = available[randrange(len(available))]
    board[x][y] = 'X'
    # The function draws the computer's move and updates the board.
    
if __name__ == "__main__":
    board = [['1','2','3'],['4','X','6'],['7','8','9']]
    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board,'O'):
            print('O wins')
            display_board(board)
            break
        draw_move(board)
        if victory_for(board,'X'):
            print('X wins')
            display_board(board)
            break
        
    

