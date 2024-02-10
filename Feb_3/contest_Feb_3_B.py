# https://atcoder.jp/contests/abc339
# Problem B
def execute():
    H = int(input())
    W = int(input())
    N = int(input())
    direction = 0
    row = 0
    column = 0
    GRID = grid(W, H)
    printedGrid = whiteOrblack(GRID, direction, row, column, N)
    print(printedGrid)

def grid(W, H):
    number_of_rows = W
    row_of_grid = []
    grid = []
    counterW = 1
    number_of_column = H
    counterH = 1
    while counterW <= number_of_rows:
        counterW += 1
        row_of_grid.append(".")
    while counterH <= number_of_column:
        counterH += 1
        grid.append(row_of_grid)
    return grid

def whiteOrblack(grid, direction, row, column, N):
    position_Takahashi = grid[row][column]
    counter = 1
    while counter < N + 1:
        if position_Takahashi == ".":
            counter += 1
            position_Takahashi = "#"
            updated_Takahashi = rotateC(direction, row, column)
            direction = updated_Takahashi[0]
            row = updated_Takahashi[1]
            column = updated_Takahashi[2]
            print(position_Takahashi)
        else:
            counter += 1
            position_Takahashi = "."
            rotateCC(direction, row, column)
            direction = updated_Takahashi[0]
            row = updated_Takahashi[1]
            column = updated_Takahashi[2]
            print(position_Takahashi)
    return grid

def rotateC(direction, row, column):
    if direction == 0:
        row = row + 1
        direction = 1
    elif direction == 1:
        column = column + 1
        direction = 2
    elif direction == 2:
        row = row - 1
        direction = 3
    elif direction == 3:
        column = column - 1
        direction = 0
    else:
        print("Error")
    return direction, row, column

def rotateCC(direction, row, column):
    if direction == 0:
        row = row - 1
        direction = 3
    elif direction == 1:
        column = column - 1
        direction = 0
    elif direction == 2:
        row = row + 1
        direction = 1
    elif direction == 3:
        column = column + 1
        direction = 2
    else:
        print("Error")
    return direction, row, column


if __name__ == '__main__':
    execute()
