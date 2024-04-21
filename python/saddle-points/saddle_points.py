def saddle_points(matrix):
    if not matrix: return matrix

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

    saddle_candidates = []

    for y in range(len(matrix)):

        for x in range(len(matrix[0])):
            column_list = [matrix[col][x] for col in range(len(matrix))]

            if matrix[y][x] == max(matrix[y]) and matrix[y][x] == min(column_list):
                saddle_candidates.append({"row": y + 1, "column": x + 1})

    return saddle_candidates
    