import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    # DP 배열 초기화
    ans = [0]*(k+1)
    # 0번째는 1로 초기화해야 누적합이 작동한다.
    ans[0] = 1
    # 각 코인(c)별로, 각 금액(i)을 채울 수 있는 경우의 수를 누적해나간다.
    for c in coins:
        # 누적합은 현재 코인으로 채울 수 있는 금액 차이일 때 이전 경우의 수를 더하는것
        for i in range(c, k+1):
            ans[i] += ans[i-c]
    # k일 때의 금액을 출력
    print(ans[-1])