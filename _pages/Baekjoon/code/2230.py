import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    A.sort() # 일단 정렬해준다.
    # 초기값은 M의 최대값으로 설정
    answer = 2000000000
    i, j = 0, 1 # i가 더 작은 수, j는 더 큰 수 (포인터)
    # j가 i보다 언제나 크니까, j가 마지막 인덱스보다 커지면 탈출
    while j < N:
        # 두 수의 차이 n
        n = A[j]-A[i]
        # M보다 클 경우,
        if n >= M:
            # 현재까지 차이와 n 중 더 작은 값을 고름
            answer = min(answer, n)
            i += 1 # 이 때는 더 작은 포인터만 움직여준다.
        # 다른 경우에는 더 큰 포인터를 움직여서 두 수 차이를 늘려줘야함(M보다 커지도록)
        else: j += 1
        # 언제나 j는 i보다 커야하니까, 만약 같아지면 j를 +1 해준다.
        if i == j: j += 1
        
    print(answer)
    
    # 메소드 체이닝 기법으로 한번에 연결
    # from itertools import combinations
    # print(min(filter(lambda x: x >= M, map(lambda x: abs(x[0]-x[1]),combinations(A, 2)))))