def minMoves(n, startRow, startCol, endRow, endCol):
    # Possible knight moves
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

    # Create a visited matrix to keep track of visited positions
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Create a queue for BFS
    queue = [(startRow, startCol, 0)]

    # Mark the starting position as visited
    visited[startRow][startCol] = True

    # Perform BFS
    while queue:
        currentRow, currentCol, movesCount = queue.pop(0)

        # Check if the ending position is reached
        if currentRow == endRow and currentCol == endCol:
            return movesCount

        # Check all possible knight moves
        for move in moves:
            newRow = currentRow + move[0]
            newCol = currentCol + move[1]

            # Check if the new position is valid and not visited
            if 0 <= newRow < n and 0 <= newCol < n and not visited[newRow][newCol]:
                queue.append((newRow, newCol, movesCount + 1))
                visited[newRow][newCol] = True

    # If the ending position cannot be reached
    return -1
