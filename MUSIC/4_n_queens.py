def n_queens_with_first(n, first_row, first_col):
    col, pos, neg = set(), set(), set()
    board = [["0"] * n for _ in range(n)]

    # Place the first queen
    board[first_row][first_col] = "1"
    col.add(first_col)
    pos.add(first_row + first_col)
    neg.add(first_row - first_col)

    def solve(r):
        if r == n:
            # If all queens are placed, print the board
            for row in board:
                print(" ".join(row))
            print()
            return

        # Skip the row if it already has the first queen
        if r == first_row:
            solve(r + 1)
            return

        for c in range(n):
            if c in col or r + c in pos or r - c in neg:
                continue

            # Place queen
            board[r][c] = "1"
            col.add(c)
            pos.add(r + c)
            neg.add(r - c)

            solve(r + 1)

            # Backtrack
            board[r][c] = "0"
            col.remove(c)
            pos.remove(r + c)
            neg.remove(r - c)

    # Start solving from row 0
    solve(0)

# Example: 8-Queens with first queen fixed at (0, 0)
n_queens_with_first(8, 0, 0)
