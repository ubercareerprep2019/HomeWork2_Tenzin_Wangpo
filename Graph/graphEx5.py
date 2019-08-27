def nbOfIslands(islandMap):

    numberOfIsland = 0
    island_width = len(islandMap[0])
    island_length = len(islandMap)
    visitedMatrix = [[0 for i in range(island_width)] for j in range(island_length)]

    for i in range(island_length):
        for j in range(island_width):
            if visitedMatrix[i][j] == 0 and islandMap[i][j] == 1:
                DFS(i, j, islandMap, visitedMatrix)
                numberOfIsland += 1

    return numberOfIsland

def check_visitedOrNot(row, col, islandMap, visitedMatrix):
        visitedMatrix[row][col] = 1
        DFS(row, col, islandMap, visitedMatrix)

def DFS(row, col, islandMap, visitedMatrix):
    if col == 0:
        if row == 0:
            if islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
                check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

            elif islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
                check_visitedOrNot(row + 1, col, islandMap, visitedMatrix)

        elif row == len(islandMap) - 1:
            if islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
                check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)

            elif islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
                check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

        else:
            if islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
                check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)

            elif islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
                check_visitedOrNot(row + 1, col, islandMap, visitedMatrix)

            elif islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
                check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

    elif col == len(islandMap[0]) - 1:
        if row == 0:
            if islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
                check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

            elif islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
                check_visitedOrNot(row + 1, col, islandMap, visitedMatrix)

        elif row == len(islandMap) - 1:
            if islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
                check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

            elif islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
                check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)

        else:
            if islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
                check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)

            elif islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
                check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

            elif islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
                check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

    elif row == 0:
        if islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
            check_visitedOrNot(row + 1, col, islandMap, visitedMatrix)

        if islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
            check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

        if islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
            check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

    elif row == len(islandMap) - 1:
        if islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
            check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)

        if islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
            check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

        if islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
            check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

    else:
        if islandMap[row][col + 1] == 1 and visitedMatrix[row][col + 1] == 0:
            check_visitedOrNot(row, col + 1, islandMap, visitedMatrix)

        if islandMap[row + 1][col] == 1 and visitedMatrix[row + 1][col] == 0:
            check_visitedOrNot(row + 1, col, islandMap, visitedMatrix)

        if islandMap[row][col - 1] == 1 and visitedMatrix[row][col - 1] == 0:
            check_visitedOrNot(row, col - 1, islandMap, visitedMatrix)

        if islandMap[row - 1][col] == 1 and visitedMatrix[row - 1][col] == 0:
            check_visitedOrNot(row - 1, col, islandMap, visitedMatrix)


island1 = [[1,1,0,0,0],
           [1,1,0,0,0],
           [0,0,1,0,0],
           [0,0,0,1,1]]

island2 = [[1,1,1,1,0],
           [1,1,0,1,0],
           [1,1,0,0,0],
           [0,0,0,0,0]]

island3 = [[1,1,0,0,1],
           [0,0,1,1,0],
           [1,1,0,0,1]]

print("the number of island in island1 is {}".format(nbOfIslands(island1)))
print("the number of island in island2 is {}".format(nbOfIslands(island2)))
print("the number of island in island3 is {}".format(nbOfIslands(island3)))

""" -------------  OUTPUT  -------------------
the number of island in island1 is 3
the number of island in island2 is 1
the number of island in island3 is 5
"""