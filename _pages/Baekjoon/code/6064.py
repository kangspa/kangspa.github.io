import sys
input = sys.stdin.readline
import math

def solution(M, N, x, y):
    # 종말의 년도 k, 현재 년도 h(x년도부터 체크)
    k, h = math.lcm(M, N), x
    
    # 종말의 날이 될 때까지 체크
    while h <= k:
        # h에서 y를 빼고 N의 배수인지 체크한다(x부터 시작해서 이미 h는 M의 배수임)
        if (h-y)%N==0: return h
        # h를 x년도부터 세니까 M을 더하면서 체크해준다.
        h += M
    # 끝까지 체크 못했다면 -1을 반환
    return -1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        print(solution(M, N, x, y))