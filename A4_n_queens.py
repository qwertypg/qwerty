def n_queens(n):
    col, pos, neg = set(), set(), set()
    board = [["0"]*n for _ in range(n)]

    def solve(r):
        if r == n:
            for row in board: print(" ".join(row))
            print()
            return
        for c in range(n):
            if c in col or r+c in pos or r-c in neg: 
                continue
            col.add(c); pos.add(r+c); neg.add(r-c)
            board[r][c] = "1"
            solve(r+1)
            board[r][c] = "0"
            col.remove(c); pos.remove(r+c); neg.remove(r-c)

    solve(0)

n_queens(8)
