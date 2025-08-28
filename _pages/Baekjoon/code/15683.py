import sys
input = sys.stdin.readline

from collections import deque
import copy

def checkVisible(board, y, x, dy, dx, N, M):
    while True:
        ny, nx = y+dy, x+dx
        # 다음이 체크 가능한 구역이라면, 7로 설정하고 y,x값 갱신
        if (0<=ny<N) & (0<=nx<M):
            if board[ny][nx]!=6:
                board[ny][nx] = 7
                y, x = ny, nx
            # 더이상 체크 불가능한 구역이라면 현재 보드를 반환
            else: return board
        else: return board

if __name__ == '__main__':
    N, M = map(int, input().split())
    CCTVS = [] # CCTV 좌표와 종류 저장
    office = [] # 현재 사무실 형태 저장
    for y in range(N):
        # 한 줄씩 입력받기
        row = list(map(int, input().split()))
        # x좌표 값과 해당 타일이 뭔지 입력받고,
        for x,c in enumerate(row):
            # 타일이 1~5 사이의 값, 즉 CCTV면 해당 좌표와 값을 넣는다.
            if c in range(1, 6): CCTVS.append((y,x,c))
        # 사무실에 입력받은 열을 넣어준다.
        office.append(row)
    # CCTV 별로 볼 수 있는 방향을 저장 (상,하,좌,우)
    one = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    two = [(1,1,0,0),(0,0,1,1)]
    three = [(1,0,0,1),(0,1,0,1),(0,1,1,0),(1,0,1,0)]
    four = [(0,1,1,1),(1,0,1,1),(1,1,0,1),(1,1,1,0)]
    five = [(1,1,1,1)]
    # cctv 방향을 전부 저장
    dirCCTV = [(), one, two, three, four, five]
    
    answer = N*M
    # CCTV가 감시가능한 구역 전부 Q에 넣는다.
    Q = deque()
    Q.append(office)
    
    for cctv in CCTVS:
        y,x,c = cctv # cctv의 좌표값과 종류
        new = deque() # 새로운 큐를 생성
        # 현재 체크해야하는 보드들
        while Q:
            board = Q.popleft()
            # 현재 cctv가 감시 가능한 방향을 7로 바꿔주는 함수에 넣는다
            for u,d,l,r in dirCCTV[c]:
                # 방향 체크하는게 전부 겹치면 안되니깐, 매번 새로운 보드를 만든다.
                nBoard = copy.deepcopy(board)
                if u: nBoard = checkVisible(nBoard, y, x, -1, 0, N, M)
                if d: nBoard = checkVisible(nBoard, y, x, 1, 0, N, M)
                if l: nBoard = checkVisible(nBoard, y, x, 0, -1, N, M)
                if r: nBoard = checkVisible(nBoard, y, x, 0, 1, N, M)
                # new 큐에 새로 만들어진 사무실을 넣어준다.
                new.append(nBoard)
        # Q가 new 큐를 가르키도록 설정해준다.(이미 Q는 비어있음)
        Q = new
    
    # Q에 남은건 전부 체크완료된 사무실뿐
    while Q:
        office = Q.popleft()
        blind = 0
        # 현재 사무실에서 사각지대는 blind에 넣기
        for row in office:
            for tile in row:
                if not tile: blind += 1
        # answer과 현재 사무실 중 사각지대 더 적은걸 넣기
        answer = min(answer, blind)
    print(answer)