import sys
input = sys.stdin.readline
# list를 슬라이싱하면 무조건 시간초과!
from collections import deque
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        P = input().rstrip()
        n = int(input())
        x = input().rstrip()
        # 빈 배열 입력해도 문자열이라 1개는 들어가므로, 예외처리해줌
        if x=='[]': x=deque([])
        else: x = deque(x[1:-1].split(','))
        
        r = 0
        for p in P:
            # deque를 사용해도 reverse연산은 많은 시간초과를 야기함
            if p=='R': r+=1 # 누적합해주고 별도 판단해준다.
            # D 연산해야할 경우,
            else:
                # 없앨 원소가 없으면 에러!
                if len(x)<=0:
                    x = 'error'
                    break
                # 뒤집어져있다면 뒤쪽 원소 삭제
                if r%2==1: x.pop()
                # 뒤집히지 않았다면 앞쪽 원소 삭제
                else: x.popleft()
        
        # 에러 발생했다면 에러만 띄워줌
        if x == 'error': print(x)
        else: # 만약 뒤집어져야하면 한번 뒤집고,
            if r%2==1: x.reverse()
            # 출력 요구조건에 맞춰서 print해준다.
            print('[',end='')
            print(*x, sep=',', end='')
            print(']')