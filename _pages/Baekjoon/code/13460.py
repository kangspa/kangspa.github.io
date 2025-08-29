import sys
input = sys.stdin.readline
# 구슬 움직임 체크 함수
def move(x, y, dx, dy):
    cnt = 0
    # 못 움직이기 전까지 +1하면서 움직여준다
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    # 각각 움직일 수 있는 좌표를 체크해둔다.
    dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
    # 큐에 2 구슬의 좌표값과 카운트 값 같이 넣어둠
    queue = []
    queue.append((rx,ry,bx,by,0))
    visited[rx][ry][bx][by] = True

    while queue:
        now = queue.pop(0)
        # 10번 이상 움직이면 체크할 필요 없다.
        if now[4] >= 10:
            continue
        # 2 구슬은 같은 방향으로 움직여야하니 4가지 방향에 대해서만 각각 체크해줌
        for xd, yd in zip(dx,dy):
            rx, ry, bx, by, cnt = now[0], now[1], now[2], now[3], now[4]
            # 전부 움직였을 때 최종 위치와 각 구슬이 움직인 횟수 체크
            rx, ry, rcnt = move(rx, ry, xd, yd)
            bx, by, bcnt = move(bx, by, xd, yd)
            cnt += 1
            # 파란게 들어갔으면 안되니까 continue
            if board[by][bx] == 'O':
                visited[rx][ry][bx][by] = True
                continue
            # 빨간게 들어갔으면 그대로 움직인 횟수 반환
            if board[ry][rx] == 'O':
                visited[rx][ry][bx][by] = True
                return cnt
            # 만약 두 구슬이 같은 위치에 있을 때,
            # 둘 중 더 많이 움직인걸 한칸 전 좌표로 바꿔준다.
            if rx == bx and ry == by:
                if rcnt > bcnt:
                    rx -= xd
                    ry -= yd
                else:
                    bx -= xd
                    by -= yd
            # 현재 두 구슬의 위치가 한번도 나온 적 없는 모양이라면 방문체크하고 큐에 넣는다.
            if visited[rx][ry][bx][by] == False:
                visited[rx][ry][bx][by] = True
                queue.append((rx, ry, bx, by, cnt))
    # 아무리 해도 통과 못하면 -1
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    # 두 구슬의 위치를 한번에 체크한다.
    visited = [[[[False] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]
    # 빨간 구슬, 파란 구슬 위치 찾아서 따로 저장하고 . 으로 바꿔준다.
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                rx, ry = x, y
                board[y][x] = '.'
            elif board[y][x] == 'B':
                bx, by = x, y
                board[y][x] = '.'
    # bfs로 탐색하고 나온 값 출력
    print(bfs(rx, ry, bx, by))