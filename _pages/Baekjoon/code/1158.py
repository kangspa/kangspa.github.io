import sys
input = sys.stdin.readline

from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    K -= 1 # K-1 만큼 회전시켜야 K번째 숫자를 꺼냄
    Q = deque(range(1, N+1)) # 1~N까지를 Q에 넣는다!
    # 출력 시작은 <
    print('<', end='')
    # Q가 끝날 때까지 반복문 시작
    while Q:
        # K-1만큼 왼쪽으로 돌려야하니 rotate(-K)
        Q.rotate(-K)
        # 현재 왼쪽 첫번째 원소가 K번째 사람(숫자)
        print(Q.popleft(), end='')
        # 만약 Q에 값이 아직 남아있다면 ', ' 넣어주기
        if len(Q): print(', ', end='')
    # 마무리
    print('>')