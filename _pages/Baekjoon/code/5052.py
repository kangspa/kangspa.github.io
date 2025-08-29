import sys
input = sys.stdin.readline

# 트라이 구조 활용
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}
        
class Trie(object):
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, lst):
        # 현재 노드 위치 가리키는 now
        now = self.head
        # 문자 하나씩 key로 잡고, 노드를 만들어서 내려감
        for c in lst:
            if c not in now.child:
                now.child[c] = Node(c)
            now = now.child[c]
        # lst의 모든 문자를 key로 해서 노드가 만들어졌으면, 마지막 노드에 data 추가
        now.data = lst
        
    def search(self, lst):
        # 현재 노드 위치 가리키는 now
        now = self.head
        # 만들어둔 트라이 구조에서 lst를 끝까지 검색
        for c in lst:
            now = now.child[c]
        # 검색 결과 하위 노드가 있다면(접두어라면) False
        if now.child: return False
        # 없다면 True
        else: return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        # 예제 1번 보면 공백은 없애는게 맞음
        phone = [input().strip().replace(' ', '') for _ in range(n)]
        
        # 각 TC에 대해 트라이 구조 생성
        trie = Trie()
        # 각 번호들을 트라이 구조에 입력
        for lst in phone: trie.insert(lst)
        # 유효한 목록인지 체크할 변수 flag
        flag = True
        # 각 번호를 검색하며, 한번이라도 유효하지 않으면 False로 변환
        for lst in phone:
            if not trie.search(lst):
                flag = False
                break
        # 유효하면 YES, 유효하지 않으면 NO
        if flag: print('YES')
        else: print('NO')

'''
# sort하면 사전순 우선 정렬 후 길이 짧은 것부터 정렬되는 특성 활용
def valid(lst):
    # 이미 정렬됐으니까, 목록에서 i-1이 i의 접두어인지만 확인하면 됨.
    for i in range(1, len(lst)):
        # 목록에서 앞 번호 길이가 뒷 번호 길이 이상이라면, 접두어가 아니니 패스
        n, m = len(lst[i-1]), len(lst[i])
        if n >= m: continue
        # i에서 n까지의 번호가 i-1의 접두어인지 체크
        if lst[i-1]==lst[i][:n]: return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        # 예제 1번 보면 공백은 없애는게 맞음
        phone = [input().strip().replace(' ', '') for _ in range(n)]
        # 우선 정렬
        phone.sort()
        # 유효한 목록이면, YES / 아니면 NO
        if valid(phone): print('YES')
        else: print('NO')
'''