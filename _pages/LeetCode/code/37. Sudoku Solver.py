class Solution(object):
    flag = False
    # return 값 없이 board 배열 값 자체를 변환해야하는게 목표
    def solveSudoku(self, board):
        self.back(board, 0, -1)
    # 백트래킹으로 탐색해보자
    def back(self, board, y, x):
        # 마지막 칸을 채운거라면 flag=True
        if (x==8) and (y==8):
            self.flag = True
            return False
        # True=뒤에서 제대로 채우지 못해서 탈출 중인 함수라는 뜻
        chk2 = False
        # 탐색마저 안 끝난 행부터 확인
        for nx in range(x+1, 9):
            if board[y][nx]==".":
                # 빈칸 채웠는지 체크 변수
                chk1 = True
                for c in range(1, 10):
                    if self.checkRow(board, y, str(c)) and self.checkCol(board, nx, str(c)) and self.checkBox(board, y, nx, str(c)):
                        board[y][nx] = str(c)
                        chk2 = self.back(board, y, nx)
                        chk1 = False
                        # 재귀 탈출 시 flag가 True면 "." 으로 안 바꿈
                        if self.flag: return False
                        board[y][nx] = "."
                if chk1 or chk2: return True
            # 끝까지 다 탐색했다면 flag=True
            if (y==8) and (nx==8):
                self.flag = True
                return
        # 다음 탐색이 필요한 열 확인 시작
        for ny in range(y+1, 9):
            for nx in range(9):
                if board[ny][nx]==".":
                    # 빈칸 채웠는지 체크 변수
                    chk1 = True
                    for c in range(1, 10):
                        if self.checkRow(board, ny, str(c)) and self.checkCol(board, nx, str(c)) and self.checkBox(board, ny, nx, str(c)):
                            board[ny][nx] = str(c)
                            chk2 = self.back(board, ny, nx)
                            chk1 = False
                            # 재귀 탈출 시 flag가 True면 "." 으로 안 바꿈
                            if self.flag: return False
                            board[ny][nx] = "."
                    if chk1 or chk2: return True
                # 끝까지 다 탐색했다면 flag=True
                if (ny==8) and (nx==8):
                    self.flag = True
                    return
    # y행에 n이 있는지
    def checkRow(self, board, y, n):
        if n in board[y]: return False
        return True
    # x열에 n이 있는지
    def checkCol(self, board, x, n):
        for i in range(9):
            if n == board[i][x]: return False
        return True
    # (y, x)가 위치한 박스에 n이 있는지
    def checkBox(self, board, y, x, n):
        yk, xk = y//3, x//3
        for ny in range(yk*3, (yk+1)*3):
            for nx in range(xk*3, (xk+1)*3):
                if n == board[ny][nx]: return False
        return True
        
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    temp = Solution()
    temp.solveSudoku(board)
    
    for row in board: print(*row)
    
    output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]