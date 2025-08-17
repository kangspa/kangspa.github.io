from collections import deque

def check_move(n, m, y, x, log, maze):
    # maze 범위 벗어나는지 체크
    if not ((0 <= y < n) & (0 <= x < m)):
        return False
    # 이미 지나온 위치인지 체크
    if log[y][x]:
        return False
    # 진행 방향에 벽이 있는지 체크
    if (maze[y][x] == 5):
        return False
    # 모든 경우 다 되면 True
    return True

def move(n, m, y, x, log, maze):
    # 수레가 갈 수 있는 방향 / 상하좌우
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    # 이동 가능한 좌표 값은 리스트에 저장
    result = []
    # 4방향으로 수레를 이동시킬 수 있는지 체크
    for i in range(4):
        dy, dx = direction[i][0], direction[i][1]
        # check_move 함수를 통해 체크하고
        if check_move(n, m, y+dy, x+dx, log, maze):
            # 유효한 위치라면 result에 추가
            result.append((y+dy, x+dx))
    # result를 반환해준다.
    return result

def bfs(maze, ry, rx, by, bx, n, m):
    # 최단 횟수 저장할 변수
    answer = 0
    
    # 방문용 배열 만들기 (ry, rx, by, bx)
    visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # 최근 기록 배열 만들기
    log_red = [[False] * m for _ in range(n)]
    log_blue = [[False] * m for _ in range(n)]
    
    # 스타트 위치는 방문으로 표시해준다.
    log_red[ry][rx] = True
    log_blue[by][bx] = True
    
    # BFS 탐색으로 최단 횟수를 알기 위해, Queue 생성
    Q = deque()
    Q.append((ry, rx, by, bx, log_red, log_blue, 0))
    
    # BFS 탐색 시작
    while Q:
        # Q의 값을 꺼내온다.
        ry, rx, by, bx, rV, bV, cnt = Q.popleft()
        # 방문한 장소라면 패스
        if visited[ry][rx][by][bx]: continue
        # 아니라면 방문 체크
        visited[ry][rx][by][bx] = True
        
        # 빨간 수레, 파란 수레 도착지점 체크 변수
        chk_r, chk_b = False, False
        # 빨간 수레가 도착지점 도착 시 True
        if maze[ry][rx] == 3: chk_r = True
        # 파란 수레가 도착지점 도착 시 True
        if maze[by][bx] == 4: chk_b = True
        
        # 둘 다 도착지점 도착 완료했다면,
        if chk_r & chk_b:
            # answer에 현재까지 카운트 저장 후 탈출
            answer = cnt
            break
        # 빨간 수레, 파란 수레 둘 다 도착 못 함
        elif ((not chk_r) & (not chk_b)):
            # 빨간 수레 유효 좌표 체크
            nrs = move(n, m, ry, rx, rV, maze)
            # 파란 수레 유효 좌표 체크
            nbs = move(n, m, by, bx, bV, maze)
        # 빨간 수레 도착, 파란 수레 미도착
        elif (chk_r & (not chk_b)):
            # 파란 수레 유효 좌표 체크
            nbs = move(n, m, by, bx, bV, maze)
            # 빨간 수레는 현위치 고정!
            nrs = [(ry, rx)]
        # 빨간 수레 미도착, 파란 수레 도착
        elif ((not chk_r) & chk_b):
            # 빨간 수레 유효 좌표 체크
            nrs = move(n, m, ry, rx, rV, maze)
            # 파란 수레는 현위치 고정!
            nbs = [(by, bx)]
        
        # 빨간 수레 이동 가능 위치와 파란 수레 이동 가능 위치 탐색
        for nry, nrx in nrs:
            for nby, nbx in nbs:
                # 현재 이동한 위치의 두 수레가 겹치면 패스
                if ((nry == nby) & (nrx == nbx)): continue
                # 만약 서로 이동한 위치가 이전 위치를 바꾼거라면 패스(겹치는 이동)
                if (((nry==by)&(nrx==bx))and((nby==ry)&(nbx==rx))): continue
                
                # 걸리는 부분 없이 이동가능하다면, 해당 위치로 옮겨준다.
                cnt += 1
                # 해당 위치 방문 체크를 해준다.
                rV[nry][nrx], bV[nby][nbx] = True, True
                # Q 에 해당위치들을 넣어준다.
                Q.append((nry, nrx, nby, nbx, rV, bV, cnt))
                
                # for 문 내에서 다음 위치들 확인할 때 누적연산 되므로
                cnt -= 1
                rV[nry][nrx], bV[nby][nbx] = False, False
    # answer 그대로 return
    return answer

def solution(maze):
    n = len(maze) # 세로 길이
    m = len(maze[0]) # 가로 길이
    
    # 수레들 스타트 위치 찾기
    for y in range(n):
        for x in range(m):
            # 빨간 수레 위치 저장
            if maze[y][x] == 1:
                ry, rx = y, x
                # 해당 위치는 빈칸으로 초기화
                maze[y][x] = 0
            # 파란 수레 위치 저장
            elif maze[y][x] == 2:
                by, bx = y, x
                # 해당 위치는 빈칸으로 초기화
                maze[y][x] = 0
    
    # BFS 탐색 함수에 넣고, 최단 횟수를 answer에 저장
    answer = bfs(maze, ry, rx, by, bx, n, m)
    return answer