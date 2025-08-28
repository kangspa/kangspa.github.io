import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T, W = map(int, input().split())
    # [시간 흐름][W번 움직일 때 획득 자두]
    DP = [[0]*(W+1) for _ in range(T+1)]
    # 매시간을 입력받고, 입력받을 때마다 DP 업데이트
    for t in range(1, T+1):
        fallen = int(input())
        # 한번도 안 움직이는 경우는 이전 값 그대로 갖고오기만 하면된다!
        DP[t][0] = DP[t-1][0] + (fallen%2)
        # t 시간 내 최대 이동횟수는 min(t+1, W+1)
        for w in range(1, min(t+1,W+1)):
            # 2번 나무 밑이라면,
            if w%2==1:
                # 이전에서 이동 안하거나, 이번에 이동한 값 중 큰값 + (fallen//2)
                DP[t][w] = max(DP[t-1][w-1], DP[t-1][w])+(fallen//2)
            # 1번 나무 밑이라면,
            else:
                # 이전에서 이동 안하거나, 이번에 이동한 값 중 큰값 + (fallen%2)
                DP[t][w] = max(DP[t-1][w-1], DP[t-1][w])+(fallen%2)
    print(max(DP[-1]))