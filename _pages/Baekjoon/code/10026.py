import sys
# 재귀 함수 최대 깊이 / N 최대값이 100이므로, 100*100으로 한계를 늘려둔다.
sys.setrecursionlimit(100**2)
input = sys.stdin.readline

# 방문체크하는 2차원 배열 안에 확인 안 한 칸이 있는지 체크하는 함수
def checkBoard(board):
    # 각 행씩 따로 체크하기 위해 for문 먼저 돌림
    for i in range(len(board)):
        # i행에 False가 있다면,
        if False in board[i]:
            # False가 있는 행과 열을 tuple 로 내보냄
            return (i, board[i].index(False))
    # 전부 체크했는데 False가 없다면, return 값을 False로 내보내서 while 문을 탈출함
    return False

# 영역 갯수 세는 함수 (2차원배열의 그림, 해당 그림의 크기, 색약 유무 bool 값)
def calcRegion(board, N, color):
    # 그림과 동일한 크기의 방문 체크 배열
    visited = [[False]*N for _ in range(N)]
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상하좌우
    # 영역의 갯수를 저장할 변수
    result = 0
    
    # 방문배열 내 가장 먼저 등장하는 False 값 위치
    s = checkBoard(visited)
    # s 값이 있으면 반복됨(False가 되면 탈출)
    while (s):
        # s는 튜플값이므로, y와 x에 나눠서 배분
        y, x = s[0], s[1]
        # 해당 위치는 방문했다고 체크
        visited[y][x] = True
        
        # c는 그림에서 실제 RGB 값
        c = board[y][x]
        # 색약이 아니면 c를 그대로 배열로 만들고C에 넣어줌
        if (not color): C = [c]
        # 색약이라면,
        else:
            # c가 R, G 중 하나라면, R, G를 동일하게 보기위해 같은 배열로 넣음
            if (c in ['R', 'G']): C = ['R', 'G']
            else: C = ['B'] # 남은 색상 하나는 B니깐 그냥 B만 배열로 해줌
        
        # 중첩 함수, visited를 인자로 안 받고 접근하기 위해 사용
        def chkV(y, x, c):
            # 4방향을 다 체크하면서
            for dy, dx in direction:
                ny, nx = y+dy, x+dx
                # 배열 범위 안인지 우선 확인
                if ((0 <= ny < N)and(0 <= nx < N)):
                    # 방문 안한 위치인지 확인하고, 같은 색상인지 확인(배열로 만들었으니 in으로 체크)
                    if ((not visited[ny][nx])and(board[ny][nx] in C)):
                        visited[ny][nx] = True # 같은 구역이라면 True
                        chkV(ny,nx,c) # dfs 로 다음 위치 탐색
        # 만들어둔 중첩함수를 시행해서 c와 같은 구역은 방문체크 해줌
        chkV(y,x,c)
        # c와 같은 구역은 전부 탐색했으니 구역 수 +1
        result += 1
        # 체크되지 않은 다음 False 위치를 찾아서 s에 넣음, 이 때 False가 없다면 s가 False가 됨
        s = checkBoard(visited)
        
    return result

if __name__ == '__main__':
    N = int(input())
    canvas = [list(input().strip()) for _ in range(N)]
    
    answer = [0,0]
    
    answer[0] = calcRegion(canvas, N, False)
    answer[1] = calcRegion(canvas, N, True)
    
    print(*answer)