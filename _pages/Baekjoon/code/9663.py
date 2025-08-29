import sys
input = sys.stdin.readline

# 백트래킹 코드
def back(N, y, answer):
    # 이번에 확인하는 퀸이 마지막 퀸이라면, +1
    if y==N:
        return answer+1
    for x in range(N):
        se, sw = y-x, y+x
        # 중복된 x거나, 대각선 위치로 영향 미치는게 있으면 넘김
        if q[x] or seL[se] or swL[sw]: continue
        # 안전위치라면 해당 위치는 방문 체크
        q[x] = seL[se] = swL[sw] = True
        # 다음으로 퀸 놓을 수 있는 위치 확인
        answer = back(N, y+1, answer)
        # 백트래킹으로 진행하니 돌아오면 False로 변경
        q[x] = seL[se] = swL[sw] = False
    return answer
# 퀸은 가로,세로 같은 줄에 한 개씩만 위치할 수 있다.
# → 세로(y) 에 대해서 for 탐색, 가로(x)에 대해서는 겹치지만 않으면 된다.
if __name__ == '__main__':
    N = int(input())
    # 퀸 위치, 남동 대각선(y-x) 유효, 남서(y+x) 대각선 유효 여부 저장
    q, seL, swL = [False]*N, [False]*(N*2-1), [False]*(N*2-1)
    # 백트래킹 돌리고, 결과 출력
    answer = back(N, 0, 0)
    print(answer)