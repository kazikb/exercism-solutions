class Matrix:
    def __init__(self, matrix_string):
        self._matrix = matrix_string.splitlines()
        for index, item in enumerate(self._matrix):
            self._matrix[index] = item.split()
            self._matrix[index] = [int(item) for item in self._matrix[index]]

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [item[index - 1] for item in self._matrix]
