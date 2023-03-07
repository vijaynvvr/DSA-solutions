def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = []
    m = len(matrix)
    n = len(matrix[0])
    totalElements = m*n

    startingRow = 0
    endingCol = n-1
    endingRow = m-1
    startingCol = 0

    count = 0
    while count < totalElements:
        # print startingRow
        for i in range(startingCol, endingCol+1):
            if count >= totalElements:
                break
            ans.append(matrix[startingRow][i])
            count += 1

        # print endingCol
        for i in range(startingRow+1, endingRow):
            if count >= totalElements:
                break
            ans.append(matrix[i][endingCol])
            count += 1

        # print endingRow
        for i in range(endingCol, startingCol-1, -1):
            if count >= totalElements:
                break
            ans.append(matrix[endingRow][i])
            count += 1

        # print startingCol
        for i in range(endingRow-1, startingRow, -1):
            if count >= totalElements:
                break
            ans.append(matrix[i][startingCol])
            count += 1

        startingRow += 1
        endingCol -= 1
        endingRow -= 1
        startingCol += 1

    return ans

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
arr = [[7],[8],[9]]

print(spiralOrder(arr))