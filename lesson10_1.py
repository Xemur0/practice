class Matrix:
    def __init__(self, list_1, list_2, list_3):
        self.list_1 = list_1
        self.list_2 = list_2
        self.list_3 = list_3

    def __add__(self):
        matr = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]
        for i in range(len(self.list_3)):
            for j in range(len(matr[i])):
                matr[i][j] = matr[i][j] + self.list_3[i][j]



        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[31, 22, 0, 0],
                    [37, 43, 0, 0],
                    [51, 86, 0, 0]],

                    [[3, 5, 32, 0],
                    [2, 4, 6, 0],
                    [-1, 64, -8, 0]],

                   [[3, 5, 8, 3],
                     [8, 3, 7, 1]])



print(my_matrix.__add__())