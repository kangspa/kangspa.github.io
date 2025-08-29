import sys
input = sys.stdin.readline
'''
1. 소수인지 확인 (에라토스테네스의 체로 소수 먼저 구하기)
2. 소수라면 계속 곱하면서 나오는 거의 소수들 체크
3. 거의 소수는 pass, 소수 아닌건 넘김
4. 최종 거의 소수 갯수 출력
'''
# 에라토스테네스의 체
def Eratos(B):
    # B의 제곱근까지만 소수인지 체크해도 됨
    l = int(B**(1/2))+1
    lst = [True]*l
    prime = []
    for n in range(2, l):
        if lst[n]:
            c = 2
            while (n*c) < l:
                lst[n*c] = False
                c += 1
            prime.append(n)
    return prime

# 단순히 n제곱하며 A 이상 B 이하인 수를 센다.
def almostPrime(A, B, prime):
    answer = 0
    for n in prime:
        i = 2
        while True:
            k = n**i
            if k > B: break
            if (A <= k <= B):
                answer += 1
            i += 1
    return answer

if __name__ == '__main__':
    A, B = map(int, input().split())
    prime = Eratos(B)
    answer = almostPrime(A, B, prime)
    print(answer)