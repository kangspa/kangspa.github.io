import sys
input = sys.stdin.readline

# 시계 방향으로 90도 회전해주기
def rotate(sticker, n, m):
    result = list([0]*n for _ in range(m))
    for i in range(n):
        for j in range(m):
            if sticker[i][j]: result[j][-(i+1)]=1
    return result

# 노트북에 스티커 붙이기
def stickOn(y, x, laptop, sticker, n, m):
    # 붙일 위치만 일단 저장
    tmp = []
    for i in range(n):
        for j in range(m):
            if ((sticker[i][j]==1) & (laptop[y+i][x+j]==0)):
                tmp.append((y+i, x+j))
            elif ((sticker[i][j]==1) & (laptop[y+i][x+j]==1)):
                return False
    # 위에서 return 안 걸렸다면, 스티커 붙이고 반환
    for y, x in tmp:
        laptop[y][x] = 1
    return laptop

# 붙이기 시도
def trySticky(laptop, N, M, sticker, n, m):
    # 회전은 총 4번
    for _ in range(4):
        # 모든 위치에서 스티커 붙이기 시도 (2단계)
        for y in range(N):
            for x in range(M):
                if ((0 <= y+n <= N) & (0 <= x+m <= M)):
                    result = stickOn(y, x, laptop, sticker, n, m)
                    if result: return result
        # 2단계 실패 시, 시계방향으로 돌려주고, 다시 2단계 반복 (3단계)
        sticker = rotate(sticker, n, m)
        # 회전하면서 스티커 가로세로가 바뀌니깐 바꿔준다.
        n, m = m, n
    # 스티커를 못 붙인다면 원래 노트북 그대로 반환
    return laptop

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    laptop = [[0]*M for _ in range(N)]
    for _ in range(K):
        n, m = map(int, input().split()) # 세로, 가로
        sticker = [list(map(int, input().split())) for _ in range(n)]
        laptop = trySticky(laptop, N, M, sticker, n, m)
    
    answer = 0
    for lap in laptop:
        for l in lap:
            answer += l
    print(answer)