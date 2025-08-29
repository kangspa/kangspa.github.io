#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int Rx, Ry, Bx, By;
    int count;
    char flag; //h==head(start), u==up, d==down, l==left, r==right, c==cannot move, t==tail(end)
    struct Node* next;
}Node;

int result = 11;

void init(char** Board, int N, int M, Node* Ball) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (Board[i][j] == 'R') {
                Ball->Ry = i;
                Ball->Rx = j;
                Board[i][j] = '.';
            }
            else if (Board[i][j] == 'B') {
                Ball->By = i;
                Ball->Bx = j;
                Board[i][j] = '.';
            }
        }
    }
    Ball->count = 0;
    Ball->flag = 'h';
    Ball->next = NULL;
}

Node* create(Node* prev) {
    Node* next;
    next = (Node*)malloc(sizeof(Node));

    next->Rx = prev->Rx;
    next->Ry = prev->Ry;
    next->Bx = prev->Bx;
    next->By = prev->By;

    next->count = prev->count + 1;
    prev->next = next;

    return(next);
}

void delete(Node* top) {
    Node* tmp;
    tmp = top;
    top = top->next;
    free(tmp);
}

void check_the_way(char** Board, Node* Ball);

void up(char** Board, Node* Ball) {
    int R = 1, B = 1;
    int c = 0;
    Node* top = create(Ball);
    while (R == 1 || B == 1) {
        if (Board[top->Ry - 1][top->Rx] == '#' || (top->Ry - 1 == top->By && top->Rx == top->Bx))
            R = 0;
        if (Board[top->By - 1][top->Bx] == '#' || (top->By - 1 == top->Ry && top->Bx == top->Rx))
            B = 0;
        if (R == 1 || B == 1) c = 1;
        if (top->Ry <= top->By) {
            if (R == 1) top->Ry--;
            if (B == 1) top->By--;
        }
        else if (top->By < top->Ry) {
            if (B == 1) top->By--;
            if (R == 1) top->Ry--;
        }
        if (Board[top->By][top->Bx] == 'O')
            return;
        if (Board[top->Ry][top->Rx] == 'O') {
            if (top->count < result) result = top->count;
            return;
        }
    }
    if (c == 1) {
        top->flag = 'u';
        check_the_way(Board, top);
    }
    else if (c == 0) {
        top->flag = 'c';
        check_the_way(Board, top);
    }
}

void down(char** Board, Node* Ball) {
    int R = 1, B = 1;
    int c = 0;
    Node* top = create(Ball);
    while (R == 1 || B == 1) {
        if (Board[top->Ry + 1][top->Rx] == '#' || (top->Ry + 1 == top->By && top->Rx == top->Bx))
            R = 0;
        if (Board[top->By + 1][top->Bx] == '#' || (top->By + 1 == top->Ry && top->Bx == top->Rx))
            B = 0;
        if (R == 1 || B == 1) c = 1;
        if (top->Ry >= top->By) {
            if (R == 1) top->Ry++;
            if (B == 1) top->By++;
        }
        else if (top->By > top->Ry) {
            if (B == 1) top->By++;
            if (R == 1) top->Ry++;
        }
        if (Board[top->By][top->Bx] == 'O')
            return;
        if (Board[top->Ry][top->Rx] == 'O') {
            if (top->count < result) result = top->count;
            return;
        }
    }
    if (c == 1) {
        top->flag = 'd';
        check_the_way(Board, top);
    }
    else if (c == 0) {
        top->flag = 'c';
        check_the_way(Board, top);
    }
}

void left(char** Board, Node* Ball) {
    int R = 1, B = 1;
    int c = 0;
    Node* top = create(Ball);
    while (R == 1 || B == 1) {
        if (Board[top->Ry][top->Rx - 1] == '#' || (top->Rx - 1 == top->Bx && top->Ry == top->By))
            R = 0;
        if (Board[top->By][top->Bx - 1] == '#' || (top->Bx - 1 == top->Rx && top->By == top->Ry))
            B = 0;
        if (R == 1 || B == 1) c = 1;
        if (top->Rx <= top->Bx) {
            if (R == 1) top->Rx--;
            if (B == 1) top->Bx--;
        }
        else if (top->Bx < top->Rx) {
            if (B == 1) top->Bx--;
            if (R == 1) top->Rx--;
        }
        if (Board[top->By][top->Bx] == 'O')
            return;
        if (Board[top->Ry][top->Rx] == 'O') {
            if (top->count < result) result = top->count;
            return;
        }
    }
    if (c == 1) {
        top->flag = 'l';
        check_the_way(Board, top);
    }
    else if (c == 0) {
        top->flag = 'c';
        check_the_way(Board, top);
    }
}

void right(char** Board, Node* Ball) {
    int R = 1, B = 1;
    int c = 0;
    Node* top = create(Ball);
    while (R == 1 || B == 1) {
        if (Board[top->Ry][top->Rx + 1] == '#' || (top->Rx + 1 == top->Bx && top->Ry == top->By))
            R = 0;
        if (Board[top->By][top->Bx + 1] == '#' || (top->Bx + 1 == top->Rx && top->By == top->Ry))
            B = 0;
        if (R == 1 || B == 1) c = 1;
        if (top->Rx >= top->Bx) {
            if (R == 1) top->Rx++;
            if (B == 1) top->Bx++;
        }
        else if (top->Bx > top->Rx) {
            if (B == 1) top->Bx++;
            if (R == 1) top->Rx++;
        }
        if (Board[top->By][top->Bx] == 'O')
            return;
        if (Board[top->Ry][top->Rx] == 'O') {
            if (top->count < result) result = top->count;
            return;
        }
    }
    if (c == 1) {
        top->flag = 'r';
        check_the_way(Board, top);
    }
    else if (c == 0) {
        top->flag = 'c';
        check_the_way(Board, top);
    }
}

void check_the_way(char** Board, Node* top) {
    if (top->flag == 'c') {
        delete(top);
        return;
    }
    if (Board[top->Ry - 1][top->Rx] != '#' && top->flag != 'd')
        up(Board, top);
    else if (Board[top->Ry + 1][top->Rx] != '#' && top->flag != 'u')
        down(Board, top);
    else if (Board[top->Ry][top->Rx - 1] != '#' && top->flag != 'r')
        left(Board, top);
    else if (Board[top->Ry][top->Rx + 1] != '#' && top->flag != 'l')
        right(Board, top);
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    getchar();

    Node* Ball;
    Ball = (Node*)malloc(sizeof(Node));

    char** Board;
    Board = (char**)calloc(N, sizeof(char*));
    for (int i = 0; i < N; i++)
        Board[i] = (char*)calloc(M, sizeof(char));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++)
            scanf("%c", &Board[i][j]);
        getchar();
    }
    init(Board, N, M, Ball);
    check_the_way(Board, Ball);
    printf("%d", result);

    return 0;
}

'''GPT가 refactoring한 코드
#include <stdio.h>

#define MAX_N 10
#define MAX_M 10

// Define structure to hold game board state
typedef struct {
    char cells[MAX_N][MAX_M];
    int red_row, red_col, blue_row, blue_col;
} board_t;

// Define recursive function to solve game
int solve(board_t board, int last_move) {
    // Check if current state is a winning or losing position
    int red_in_goal = 0, blue_in_goal = 0;
    for (int i = 0; i < MAX_N; i++) {
        for (int j = 0; j < MAX_M; j++) {
            if (board.cells[i][j] == 'R') {
                if (i == board.red_row && j == board.red_col) {
                    red_in_goal = 1;
                }
            } else if (board.cells[i][j] == 'B') {
                if (i == board.blue_row && j == board.blue_col) {
                    blue_in_goal = 1;
                }
            }
        }
    }
    if (red_in_goal && !blue_in_goal) {
        return 1; // Red ball in goal, game won
    } else if (blue_in_goal || last_move == 10) {
        return -1; // Blue ball in goal or too many moves, game lost
    }

    // Loop through possible directions
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    for (int i = 0; i < 4; i++) {
        // Simulate moving balls in this direction
        int red_new_row = board.red_row + directions[i][0];
        int red_new_col = board.red_col + directions[i][1];
        int blue_new_row = board.blue_row + directions[i][0];
        int blue_new_col = board.blue_col + directions[i][1];

        // Check if red ball can move in this direction
        if (board.cells[red_new_row][red_new_col] == '.') {
            // Move red ball
            board.cells[board.red_row][board.red_col] = '.';
            board.cells[red_new_row][red_new_col] = 'R';
            board.red_row = red_new_row;
            board.red_col = red_new_col;

            // Check if blue ball can move in this direction
            if (board.cells[blue_new_row][blue_new_col] == '.') {
                // Move blue ball
                board.cells[board.blue_row][board.blue_col] = '.';
                board.cells[blue_new_row][blue_new_col] = 'B';
                board.blue_row = blue_new_row;
                board.blue_col = blue_new_col;

                // Check if resulting state is valid
                int valid = 1;
                if (red_new_row == blue_new_row && red_new_col == blue_new_col) {
                    if (i == 0) { // Up
                        valid = board.red_row < board.blue_row;
                    } else if (i == 1) { // Down
                        valid = board.red_row > board.blue_row;
                    } else if (i == 2) { // Left
                        valid = board.red_col < board.blue_col;
                    } else if (i == 3) { // Right
                        valid = board.red_col > board.blue_col;
                    }
                    if (!valid) {
                        // Move blue ball back
                        board.cells[board.blue_row][board.blue_col] = '.';
                        board.cells[blue_new_row - directions[i][0]][blue_new_col - directions[i][1]] = 'B';
                        board.blue_row -= directions[i][0];
                        board.blue_col -= directions[i][1];
                    }
                }

                // If resulting state is valid, recursively call function
                if (valid) {
                    int result = solve(board, i);
                    if (result == 1) {
                        return 1;
                    }
                }
            }
            // If blue ball cannot move, move red ball back
            board.cells[board.red_row][board.red_col] = '.';
            board.cells[red_new_row - directions[i][0]][red_new_col - directions[i][1]] = 'R';
            board.red_row -= directions[i][0];
            board.red_col -= directions[i][1];
        }
    }
    // If none of the recursive calls returned a winning position, return -1
    return -1;
}

int main() {
    // Read input and initialize game board state
    int n, m;
    scanf("%d %d", &n, &m);
    board_t board;
    for (int i = 0; i < n; i++) {
        scanf("%s", board.cells[i]);
        for (int j = 0; j < m; j++) {
            if (board.cells[i][j] == 'R') {
                board.red_row = i;
                board.red_col = j;
            }
            else if (board.cells[i][j] == 'B') {
                board.blue_row = i;
                board.blue_col = j;
            }
        }
    }
    printf(solve(board, 0));
    return 0;
}
'''