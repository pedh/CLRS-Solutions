class MatrixException(Exception):
    message = "unknown matrix error"

    def __init__(self, msg, *args, **kwargs):
        message = (msg % args) % kwargs
        super(MatrixException, self).__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class Matrix(object):
    def __init__(self, lst, row, column):
        if len(lst) != row * column:
            raise MatrixException("bad matrix: length %(length)s, row %(row)s,"
                                  " column %(column)s",
                                  length=len(lst),
                                  row=row,
                                  column=column)
        self.v = lst
        self.r = row
        self.c = column

    def __repr__(self):
        return "\n".join(
            (" ".join(str(val)
                      for val in self.v[r * self.c: (r + 1) * self.c]))
            for r in range(self.r))

    def value(self, r, c):
        idx = r * self.c + c
        if idx >= len(self.v):
            raise MatrixException("out of range: row %(row)s, column "
                                  "%(column)s", row=r, column=c)
        return self.v[idx]

    def update(self, r, c, val):
        idx = r * self.c + c
        if idx >= len(self.v):
            raise MatrixException("out of range: row %(row)s, column "
                                  "%(column)s", row=r, column=c)
        self.v[idx] = val

    def __mul__(self, m):
        if self.c != m.r:
            raise MatrixException("Invalid Matrix multiplication: "
                                  "(%(row)s*%(column)s) matrix * "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.r,
                                  column=self.c,
                                  mrow=m.r,
                                  mcolumn=m.c)
        pv = [0] * (self.r * m.c)
        for i in range(self.r):
            for j in range(m.c):
                val = 0
                for k in range(self.c):
                    val += self.value(i, k) * m.value(k, j)
                pv[i * self.c + j] = val
        return Matrix(pv, self.r, m.c)

    def __add__(self, m):
        if self.r != m.r or self.c != m.c:
            raise MatrixException("Invalid Matrix addition: "
                                  "(%(row)s*%(column)s) matrix + "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.r,
                                  column=self.c,
                                  mrow=m.r,
                                  mcolumn=m.c)
        pv = [0] * (self.r * self.c)
        for i in range(self.r):
            for j in range(self.c):
                pv[i * self.c + j] = self.value(i, j) + m.value(i, j)
        return Matrix(pv, self.r, self.c)

    def __sub__(self, m):
        if self.r != m.r or self.c != m.c:
            raise MatrixException("Invalid Matrix addition: "
                                  "(%(row)s*%(column)s) matrix + "
                                  "(%(mrow)s*%(mcolumn)s) matrix",
                                  row=self.r,
                                  column=self.c,
                                  mrow=m.r,
                                  mcolumn=m.c)
        pv = [0] * (self.r * self.c)
        for i in range(self.r):
            for j in range(self.c):
                pv[i * self.c + j] = self.value(i, j) - m.value(i, j)
        return Matrix(pv, self.r, self.c)


def sub_matrix(m, r0, c0, rl, cl):
    lst = [m.value(i, j)
           for i in range(r0, r0 + rl)
           for j in range(c0, c0 + cl)]
    return Matrix(lst, rl, cl)


def add_zero_edge_matrix(m):
    lst = [0] * (m.c + 1)
    for i in range(m.r):
        lst.append(0)
        lst += m.v[i * m.c: (i + 1) * m.c]
    return Matrix(lst, m.r + 1, m.c + 1)


def sm(m1, m2):
    if not(m1.r == m1.c == m2.r == m2.c):
        return None
    n = m1.r
    if n < 3:
        return m1 * m2
    is_even_matrix = not n % 2
    if not is_even_matrix:
        n += 1
        m1 = add_zero_edge_matrix(m1)
        m2 = add_zero_edge_matrix(m2)
    hn = n // 2
    m111 = sub_matrix(m1, 0, 0, hn, hn)
    m112 = sub_matrix(m1, 0, hn, hn, hn)
    m121 = sub_matrix(m1, hn, 0, hn, hn)
    m122 = sub_matrix(m1, hn, hn, hn, hn)
    m211 = sub_matrix(m2, 0, 0, hn, hn)
    m212 = sub_matrix(m2, 0, hn, hn, hn)
    m221 = sub_matrix(m2, hn, 0, hn, hn)
    m222 = sub_matrix(m2, hn, hn, hn, hn)
    s1 = m212 - m222
    s2 = m111 + m112
    s3 = m121 + m122
    s4 = m221 - m211
    s5 = m111 + m122
    s6 = m211 + m222
    s7 = m112 - m122
    s8 = m221 + m222
    s9 = m111 - m121
    s10 = m211 + m212
    p1 = sm(m111, s1)
    p2 = sm(s2, m222)
    p3 = sm(s3, m211)
    p4 = sm(m122, s4)
    p5 = sm(s5, s6)
    p6 = sm(s7, s8)
    p7 = sm(s9, s10)
    p11 = p5 + p4 - p2 + p6
    p12 = p1 + p2
    p21 = p3 + p4
    p22 = p5 + p1 - p3 - p7
    v = [0] * n * n
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            if i < hn:
                if j < hn:
                    v[idx] = p11.value(i, j)
                else:
                    v[idx] = p12.value(i, j - hn)
            else:
                if j < hn:
                    v[idx] = p21.value(i - hn, j)
                else:
                    v[idx] = p22.value(i - hn, j - hn)
    m = Matrix(v, n, n)
    if is_even_matrix:
        return m
    return sub_matrix(m, 1, 1, n - 1, n - 1)


def main():
    n = 9
    mx = Matrix(list(range(n * n)), n, n)
    mx1 = Matrix(list(range(10, n * n + 10)), n, n)
    print(mx)
    print(mx1)
    print(mx * mx1)
    print(sm(mx, mx1))


if __name__ == "__main__":
    main()
