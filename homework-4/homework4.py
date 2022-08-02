
def search_in_matrix(matrix, target):

    number_of_columns = len(matrix)
    row = 0
    column = number_of_columns - 1
    while row < number_of_columns and column >= 0:
        if matrix[row][column] == target:
            print([row, column])
            return 1

        if matrix[row][column] > target:
            column -= 1
        else:
            row += 1

    print([-1, -1])
    return 0

# Matrix does not have the same height & width
matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
    [201, 208, 209, 210, 245, 1005]]

target = 201
# Output is [5, 0]

# target = 44
# Output is [3, 3]

# target = 207
# Output is [-1, -1]

search_in_matrix(matrix, target)


