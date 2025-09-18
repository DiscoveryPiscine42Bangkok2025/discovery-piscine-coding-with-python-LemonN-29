def checkmate(board):
    try:
        board_list = [list(row.strip()) for row in board.splitlines()]
        num_row = len(board_list)
        
        # ceck number row columns 
        if num_row == 0 or any(len(row) != num_row for row in board_list):
            print("fail")
            print("Board must be square and non-empty.")
            return
        
        # where are you king ?
        king_pos = None
        for i in range(num_row):
            for j in range(num_row):
                if board_list[i][j].upper() == "K":
                    king_pos = (i, j)

        if king_pos is None:
            print("Fail")
            return

        # x, y
        x_k, y_k = king_pos

        directions_rook = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        directions_bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        pawn_moves = [(1, -1), (1, 1)] 

        # check if in bounds
        def in_bounds(x, y):
            return 0 <= x < num_row and 0 <= y < num_row

        def check_dir(directions, pieces, one_step=False):
            """Check directions for pieces. If one_step=True, only check one square."""
            for dx, dy in directions:
                x, y = x_k + dx, y_k + dy
                while in_bounds(x, y):
                    if board_list[x][y] != '.':
                        if board_list[x][y].upper() in pieces:
                            return True
                        break
                    if one_step:
                        break
                    x += dx
                    y += dy
            return False

        if check_dir(pawn_moves, {'P'}, one_step=True):
            print("Success (Pawn)")
            return

        if check_dir(directions_rook, {'R', 'Q'}):
            print("Success (Rook/Queen)")
            return

        if check_dir(directions_bishop, {'B', 'Q'}):
            print("Success (Bishop/Queen)")
            return

        print("Fail")

    except Exception as e:
        print("Fail", e)