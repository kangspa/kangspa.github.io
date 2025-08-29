import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    # 투 포인터 / i, j < N
    i, j = 0, 0
    # 누적합 now
    now = lst[i]
    # 부분합 길이 초기 값
    answer = N+1
    while True:
        # 합이 S 이상이면, 답 갱신(길이에 자신도 포함해야하니 +1)
        if now >= S:
            answer = min(answer, j-i+1)
            # i를 한 칸 앞으로 옮기면서, 이전 i값은 빼줌
            now -= lst[i]
            i += 1
            # i가 j보다 커지면 최소 n(1)이 구해진 것
            if i > j: break
        # 합이 S 미만이면 부분합 길이를 늘리기 위해 j+1
        else:
            j += 1
            # j 가 N보다 작을 때는, now에 j 위치 값만큼 더해준다.
            if j < N: now += lst[j]
            # j가 N 이상이라면, 더이상 부분합으로 S 이상 못 만든다는 것
            else: break
    # 초기값 그대로라면 0, 아니면 answer
    answer = answer if answer != (N+1) else 0
    print(answer)