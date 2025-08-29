import sys
input = sys.stdin.readline

# 파이배열 : 문자열에서 패턴을 찾고,
# 접두사와 접미사가 해당 위치에서 몇번째까지 같은지 찾는 알고리즘
def piList(pattern):
    n = len(pattern)
    # 파이배열 초기화
    pi = [0]*n
    # i=전체에서 시작위치, j=현재 체크해야할 마지막 위치
    i = 0
    for j in range(1, n):
        # 만약 다를 경우, i가 0이 될 때까지 초기화
        # 초기화는 파이배열에서 이전까지의 반복위치 값을 찾아가며 초기화해준다.
        # 만약 i번째 문자와 j번째 문자가 같다면, 그 순간부터는 다음 값을 비교해준다.
        while i > 0 and pattern[i] != pattern[j]:
            i = pi[i-1]
        # 같으면, i를 1더하고 파이배열에 이전까지의 값은 동일했음을 저장
        if pattern[i] == pattern[j]:
            i += 1
            pi[j]=i
    # 만들어진 파이배열 리턴
    return pi

def KMP(T, P):
    n, m = len(T), len(P)
    # 먼저 파이배열을 만들어서 패턴을 찾는다.
    pi = piList(P)
    # 결과가 저장될 배열
    res = []
    # i=P에서 체크해야하는 값이 있는 위치, j=T에서 체크해야하는 위치
    i = 0
    for j in range(n):
        # 서로 다르다면, 파이배열 찾을 때와 동일하게 진행
        # 같은 문자가 나올 때까지 P에서 비교하는 문자를 하나씩 이전까지 같았던 값으로 변경
        while i > 0 and P[i] != T[j]:
            i = pi[i-1]
        # 서로 같을 경우, P에서 비교하는 문자를 하나씩 더해줌(j는 for문으로 인해 계속 +1 됨)
        if P[i] == T[j]:
            i += 1
            # 만약 P를 끝까지 체크했다면, res에 저장하고 해당위치에서 동일문자가 있던 위치까지 이동
            if i == m:
                res.append(j-i+1)
                i = pi[i-1]
    
    return res

if __name__ == '__main__':
    # strip을 하면 문장 시작이 공백으로 시작할 경우 사라져버림 > rstrip으로!
    T = '0' + input().rstrip()
    P = input().rstrip()
    
    ans = KMP(T, P)
        
    # 출력
    print(len(ans))
    for a in ans:
        print(a, end=' ')
#############################################################
# 해당 방식은 예상했지만 시간 초과임
'''
if __name__ == '__main__':
    T = input().strip()
    P = input().strip()
    
    ansN = 0
    ansIdx = []
    
    while True:
        ans = T.find(P)
        # -1일 경우, T 안에서 P를 찾지 못한다.
        if ans==-1: break
        # 위치를 찾았다면 해당 위치를 저장
        ansN += 1
        # 저장은 가장 마지막 값에서 찾은 인덱스 값을 더해서 진행
        if ansIdx: ansIdx.append(ansIdx[-1]+ans+1)
        # 처음이라면 1을 더해서 저장
        else: ansIdx.append(ans+1)
        # 자르고 다시 체크
        T = T[ans+1:]
    # 출력
    print(ansN)
    for n in ansIdx:
        print(n, end=' ')
'''