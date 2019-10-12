# pylint: disable=too-many-locals, too-many-statements

"""
Matrix multiplication.
"""


class MatrixException(Exception):
    """Matrix exception class."""
    message = "unknown matrix error"

    def __init__(self, msg, *args, **kwargs):
        message = (msg % args) % kwargs
        super(MatrixException, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class Matrix:
    """Matrix class."""
    def __init__(self, lst, row, column):
        if len(lst) != row * column:
            raise MatrixException("bad matrix: length %(length)s, row %(row)s,"
                                  " column %(column)s",
                                  length=len(lst),
                                  row=row,
                                  column=column)
        self.lst = lst
        self.row = row
        self.column = column

    def __repr__(self):
        return "\n".join(
            (" ".join(str(val)
                      for val
                      in self.lst[i * self.column: (i + 1) * self.column]))
            for i in range(self.row))

    def value(self, row, column):
        """The value of element indexed by specified row and column."""
        idx = row * self.column + column
        if idx >= len(self.lst):
            raise MatrixException("out of range: row %(row)s, column "
                                  "%(column)s", row=row, column=column)
        return self.lst[idx]

    def update(self, row, column, val):
        """Update the value of element indexed by specified row and column."""
        idx = row * self.column + column
        if idx >= len(self.lst):
            raise MatrixException("out of range: row %(row)s, column "
                                  "%(column)s", row=row, column=column)
        self.lst[idx] = val

    def __mul__(self, mtx):
        if self.column != mtx.row:
            raise MatrixException("Invalid Matrix multiplication: "
                                  "(%(row)s*%(column)s) matrix * "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.row,
                                  column=self.column,
                                  mrow=mtx.row,
                                  mcolumn=mtx.column)
        p_lst = [0] * (self.row * mtx.column)
        for i in range(self.row):
            for j in range(mtx.column):
                val = 0
                for k in range(self.column):
                    val += self.value(i, k) * mtx.value(k, j)
                p_lst[i * self.column + j] = val
        return Matrix(p_lst, self.row, mtx.column)

    def __add__(self, mtx):
        if self.row != mtx.row or self.column != mtx.column:
            raise MatrixException("Invalid Matrix addition: "
                                  "(%(row)s*%(column)s) matrix + "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.row,
                                  column=self.column,
                                  mrow=mtx.row,
                                  mcolumn=mtx.column)
        s_lst = [0] * (self.row * self.column)
        for i in range(self.row):
            for j in range(self.column):
                s_lst[i * self.column + j] = self.value(i, j) + mtx.value(i, j)
        return Matrix(s_lst, self.row, self.column)

    def __sub__(self, mtx):
        if self.row != mtx.row or self.column != mtx.column:
            raise MatrixException("Invalid Matrix addition: "
                                  "(%(row)s*%(column)s) matrix + "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.row,
                                  column=self.column,
                                  mrow=mtx.row,
                                  mcolumn=mtx.column)
        d_lst = [0] * (self.row * self.column)
        for i in range(self.row):
            for j in range(self.column):
                d_lst[i * self.column + j] = self.value(i, j) - mtx.value(i, j)
        return Matrix(d_lst, self.row, self.column)


def submatrix(mtx, row_base, column_base, row_count, column_count):
    """Submatrix."""
    lst = [mtx.value(i, j)
           for i in range(row_base, row_base + row_count)
           for j in range(column_base, column_base + column_count)]
    return Matrix(lst, row_count, column_count)


def add_zero_edge_matrix(mtx):
    """Add an zero edge to the matrix."""
    lst = [0] * (mtx.column + 1)
    for i in range(mtx.row):
        lst.append(0)
        lst += mtx.lst[i * mtx.column: (i + 1) * mtx.column]
    return Matrix(lst, mtx.row + 1, mtx.column + 1)


def strassen_method(mtx1, mtx2):
    """Strassen's method of matrix multiplication."""
    if not mtx1.row == mtx1.column == mtx2.row == mtx2.column:
        return None
    size = mtx1.row
    if size < 3:
        return mtx1 * mtx2
    is_even_matrix = not size % 2
    if not is_even_matrix:
        # The size of matrix is not even.
        size += 1
        mtx1 = add_zero_edge_matrix(mtx1)
        mtx2 = add_zero_edge_matrix(mtx2)
    mid = size // 2
    mtx111 = submatrix(mtx1, 0, 0, mid, mid)
    mtx112 = submatrix(mtx1, 0, mid, mid, mid)
    mtx121 = submatrix(mtx1, mid, 0, mid, mid)
    mtx122 = submatrix(mtx1, mid, mid, mid, mid)
    mtx211 = submatrix(mtx2, 0, 0, mid, mid)
    mtx212 = submatrix(mtx2, 0, mid, mid, mid)
    mtx221 = submatrix(mtx2, mid, 0, mid, mid)
    mtx222 = submatrix(mtx2, mid, mid, mid, mid)
    sum1 = mtx212 - mtx222
    sum2 = mtx111 + mtx112
    sum3 = mtx121 + mtx122
    sum4 = mtx221 - mtx211
    sum5 = mtx111 + mtx122
    sum6 = mtx211 + mtx222
    sum7 = mtx112 - mtx122
    sum8 = mtx221 + mtx222
    sum9 = mtx111 - mtx121
    sum10 = mtx211 + mtx212
    product1 = strassen_method(mtx111, sum1)
    product2 = strassen_method(sum2, mtx222)
    product3 = strassen_method(sum3, mtx211)
    product4 = strassen_method(mtx122, sum4)
    product5 = strassen_method(sum5, sum6)
    product6 = strassen_method(sum7, sum8)
    product7 = strassen_method(sum9, sum10)
    product11 = product5 + product4 - product2 + product6
    product12 = product1 + product2
    product21 = product3 + product4
    product22 = product5 + product1 - product3 - product7
    lst = [0] * size * size
    for i in range(size):
        for j in range(size):
            idx = i * size + j
            if i < mid:
                if j < mid:
                    lst[idx] = product11.value(i, j)
                else:
                    lst[idx] = product12.value(i, j - mid)
            else:
                if j < mid:
                    lst[idx] = product21.value(i - mid, j)
                else:
                    lst[idx] = product22.value(i - mid, j - mid)
    mtx = Matrix(lst, size, size)
    if is_even_matrix:
        return mtx
    return submatrix(mtx, 1, 1, size - 1, size - 1)


def main():
    """The main function."""
    size = 9
    mtx1 = Matrix(list(range(size * size)), size, size)
    mtx2 = Matrix(list(range(10, size * size + 10)), size, size)
    print(mtx1)
    print()
    print(mtx2)
    print()
    print(mtx1 * mtx2)
    print()
    print(strassen_method(mtx1, mtx2))


if __name__ == "__main__":
    main()
