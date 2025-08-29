import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    coordiate = [tuple(map(int, input().split())) for _ in range(N)]
    # 파이썬 정렬 함수는 문제 요구사항을 그대로 따라준다.
    for x, y in sorted(coordiate): print(x, y)