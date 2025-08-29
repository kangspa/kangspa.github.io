import sys
input = sys.stdin.readline
from collections import deque

def countArea(sy, sx, visited, paper, n, m):
    # (y, x) : 상하좌우
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    Q = deque()
    Q.append((sy, sx))
    area = 0 # 현재 그림의 넓이
    while Q:
        y, x = Q.popleft()
        # 체크한 위치면 넘김
        if visited[y][x]: continue
        # 체크 안한 칸이면 체크하고, 넓이 더해주기
        visited[y][x] = True
        area += 1
        # 주변 칸 탐색
        for dy, dx in direction:
            ny, nx = y+dy, x+dx
            if ((0 <= ny < n) & (0 <= nx < m)):
                # 그림 그려진 칸일 경우 확인을 위해 Q에 추가
                if paper[ny][nx]: Q.append((ny, nx))
    # 그림 넓이 세기 끝났다면 반환
    return visited, paper, area

if __name__=='__main__':
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    drawNum = 0
    drawArea = 0
    # 1이 그려진 칸이라면, countArea로 그림의 넓이를 세준다.
    for y in range(n):
        for x in range(m):
            if ((not visited[y][x]) & paper[y][x]):
                drawNum += 1
                visited, paper, area = countArea(y, x, visited, paper, n, m)
                drawArea = max(drawArea, area)
    print(drawNum)
    print(drawArea)