import sys
input = sys.stdin.readline

from collections import deque
import copy

def move_left(NOW):
    board = copy.deepcopy(NOW)
    N = len(board)
    for y in range(N):
        index = deque(list(range(N)))
        value = 0
        for x in range(N):
            if board[y][x] > 0 and value == 0:
                while index:
                    pos = index.popleft()
                    if board[y][pos] == 0 or pos == x: break
                value, board[y][x] = board[y][x], 0
            elif board[y][x] > 0 and value != 0:
                if board[y][x] == value:
                    value += board[y][x]
                    board[y][x] = 0

                    board[y][pos], value = value, 0
                elif board[y][x] != value:
                    board[y][pos] = value
                    while index:
                        pos = index.popleft()
                        if board[y][pos] == 0 or pos == x: break
                    value, board[y][x] = board[y][x], 0
        if value != 0:
            board[y][pos] = value
    return board

def move_right(NOW):
    board = copy.deepcopy(NOW)
    N = len(board)
    for y in range(N):
        index = deque(list(range(N)))
        value = 0
        for x in range(N-1, -1, -1):
            if board[y][x] > 0 and value == 0:
                while index:
                    pos = index.pop()
                    if board[y][pos] == 0 or pos == x: break
                value, board[y][x] = board[y][x], 0
            elif board[y][x] > 0 and value != 0:
                if board[y][x] == value:
                    value += board[y][x]
                    board[y][x] = 0

                    board[y][pos], value = value, 0
                elif board[y][x] != value:
                    board[y][pos] = value
                    while index:
                        pos = index.pop()
                        if board[y][pos] == 0 or pos == x: break
                    value, board[y][x] = board[y][x], 0
        if value != 0:
            board[y][pos] = value
    return board

def move_up(NOW):
    board = copy.deepcopy(NOW)
    N = len(board)
    for x in range(N):
        index = deque(list(range(N)))
        value = 0
        for y in range(N):
            if board[y][x] > 0 and value == 0:
                while index:
                    pos = index.popleft()
                    if board[pos][x] == 0 or pos == y: break
                value, board[y][x] = board[y][x], 0
            elif board[y][x] > 0 and value != 0:
                if board[y][x] == value:
                    value += board[y][x]
                    board[y][x] = 0

                    board[pos][x], value = value, 0
                elif board[y][x] != value:
                    board[pos][x] = value
                    while index:
                        pos = index.popleft()
                        if board[pos][x] == 0 or pos == y: break
                    value, board[y][x] = board[y][x], 0
        if value != 0:
            board[pos][x] = value
    return board

def move_down(NOW):
    board = copy.deepcopy(NOW)
    N = len(board)
    for x in range(N):
        index = deque(list(range(N)))
        value = 0
        for y in range(N-1, -1, -1):
            if board[y][x] > 0 and value == 0:
                while index:
                    pos = index.pop()
                    if board[pos][x] == 0 or pos == y: break
                value, board[y][x] = board[y][x], 0
            elif board[y][x] > 0 and value != 0:
                if board[y][x] == value:
                    value += board[y][x]
                    board[y][x] = 0

                    board[pos][x], value = value, 0
                elif board[y][x] != value:
                    board[pos][x] = value
                    while index:
                        pos = index.pop()
                        if board[pos][x] == 0 or pos == y: break
                    value, board[y][x] = board[y][x], 0
        if value != 0:
            board[pos][x] = value
    return board

def print_board(board):
    MAX = max(map(max, board))
    for y in range(len(board)):
        for x in range(len(board)):
            print(f'{board[y][x]:>{len(str(MAX))}d}', end=' ')
        print()
    print()


N = int(input())
origin_board = [list(map(int, input().split( ))) for _ in range(N)]
used_board = []

Q = deque()
Q.append((origin_board, 0))

answer = 0
while Q:
    now_board, cnt = Q.popleft()
    if not now_board in used_board and cnt < 5:
        used_board.append(now_board)

        board = move_left(now_board)
        MAX = max(map(max, board))
        answer = MAX if MAX > answer else answer
        Q.append((board, cnt+1))

        board = move_right(now_board)
        MAX = max(map(max, board))
        answer = MAX if MAX > answer else answer
        Q.append((board, cnt+1))

        board = move_up(now_board)
        MAX = max(map(max, board))
        answer = MAX if MAX > answer else answer
        Q.append((board, cnt+1))

        board = move_down(now_board)
        MAX = max(map(max, board))
        answer = MAX if MAX > answer else answer
        Q.append((board, cnt+1))
print(answer)