import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    
    a.sort() # 일단 정렬
    # a의 인덱스 값(i<j), 양끝에서 조사한다!
    i, j = 0, n-1
    # 숫자쌍의 갯수
    answer = 0
    # i가 j보다 작을 때 작동하도록 함, 즉 두 인덱스값이 만나면 종료
    while i<j:
        # 두 숫자합이 x와 같다면,
        if a[i]+a[j] == x:
            answer += 1 # 더해주고
            j -= 1 # j를 1 빼주거나, i를 1 더해주거나
        # 두 숫자합이 x보다 작다면
        elif a[i]+a[j] < x:
            i += 1 # 합이 커져야하니 i+1
        # 두 숫자합이 x보다 크다면
        elif a[i]+a[j] > x:
            j -= 1 # 합이 작아져야하니 j-1
    print(answer)