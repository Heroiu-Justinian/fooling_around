#include <iostream>
#include <stdlib.h>



enum State {TTT_O = 1, TTT_X = 2};
int Board[3][3];

void init(int board[][3]);
void display(int board[][3]);
bool matches(int a, int b, int c);
bool make_move(int board[][3], int row, int col, int turn);
int check_winner(int board[][3]);



int main(){
    int row,col,turn = 0;
    int end = 0;
    bool moved = false;
    init(Board);
    display(Board);
    while(!end && turn < 9){
        std::cin >> row >> col;
        while(!moved){
            moved = make_move(Board,row,col,turn);
        }
        end = check_winner(Board);
        turn ++;
        moved = false;
        display(Board);
    }
    std::cout << check_winner(Board)<<std::endl;
}

void init(int board[][3]){
    int i,j;
    for(i = 0;i < 3;i++ ){
        for(j = 0;j< 3;j++){
            board[i][j] = 0;
        }
    }
}


void display(int board[][3]){
   int i,j;
    std::cout << "- - - - - - ";
    std::cout << std::endl;

    for(i = 0;i < 3;i++ ){
        for(j = 0;j< 3;j++){
            if(board[i][j] == TTT_O)
                std::cout <<"|O|"<<" ";
            else if(board[i][j] == TTT_X)
                std::cout << "|X|"<<" ";
            else{
                std::cout << "| |" << " ";
            }
            
        }
        std::cout << std::endl;
        std::cout << "- - - - - - ";
        std::cout << std::endl;
        
    }
}

bool make_move(int board[][3], int row, int col, int turn){
    int move;
    int move_made = false;
    if(turn % 2 == 0){
        move = TTT_X;
    }
    else 
    {
        move = TTT_O;
    }
        if(board[row][col] == 0)
        {
            board[row][col] = move;
            move_made = true;
        }
        else{
            std::cout << "Invalid move"<<std::endl;
            return move_made;
        }
        
}

int check_winner(int board[][3]){
    int i;
    //horizontal
    for(i = 0;i<3;i++){
        if(matches(board[i][0],board[i][1],board[i][2])){
            return board[i][0];
        }
    }
    //vertical
    for(i = 0;i<3;i++){
        if(matches(board[0][i],board[1][i],board[2][i])){
            return board[0][i];
        }
    }
    //diagonal
        if((matches(board[0][0],board[1][1],board[2][2])) or matches(board[0][2],board[1][1],board[2][0])){
            return board[1][1];
    }
    return 0;
}

bool matches(int a, int b, int c){
    if(a != 0 && b != 0 && c !=0){
        return a == b && b == c && a == c;
    }
    return false;
}