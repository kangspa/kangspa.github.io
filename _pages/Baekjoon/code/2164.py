import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    N = int(input())
    Q = deque(range(1, N+1))
    # 현재 해야하는 연산 체크용
    chk = True
    while True:
        n = Q.popleft()
        # Q가 비었으면 마지막에 뽑은 숫자 출력
        if not Q:
            print(n)
            break
        # 시작은 버리고, 다음부터 우측에 넣는다.
        if chk: chk = False
        else:
            Q.append(n)
            chk = True