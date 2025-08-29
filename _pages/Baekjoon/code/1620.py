import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    # 하나씩 dict 형태로 입력받는다.
    lib = dict()
    for i in range(1, N+1):
        lib[i] = input().rstrip()
    # 생성된 lib의 키, 값 반전
    rlib = {v:k for k,v in lib.items()}
    # 문제 입력받고, 바로 답 출력
    for _ in range(M):
        q = input().rstrip()
        if q[0] in '123456789':
            q = int(q)
            print(lib[q])
        else:
            print(rlib[q])