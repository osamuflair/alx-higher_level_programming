'''
a matrix
multiplication
'''
def matrix_mul(m_a, m_b):
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for n in m_a:
        if type(n) != list:
            raise TypeError("m_a must be a list of lists")
    for n in m_b:
        if type(n) != list:
            raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise ValueError("m_a can't be empty")
    for n in m_a:
        if not n:
            raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    for n in m_b:
        if not n:
            raise ValueError("m_b can't be empty")
    b = 0
    d = 0
    for n in range(len(m_a)):
        d += 1
        for m in m_a[n]:
            b += 1
            if type(m) != int and type(m) != float:
                raise TypeError("m_a should contain only integers or floats")
    e = int(b / d)
    for n in range(len(m_b)):
        for m in m_b[n]:
            if type(m) != int and type(m) != float:
                raise TypeError("m_b should contain only integers or floats")
    for n in range(len(m_a)):
        if n != len(m_a) - 1:
            if len(m_a[n]) != len(m_a[n + 1]):
                raise TypeError("each row of m_a must be of the same size")
    a = 0
    for n in range(len(m_b)):
        a += 1
        if n != len(m_b) - 1:
            if len(m_b[n]) != len(m_b[n + 1]):
                raise TypeError("each row of m_b must be of the same size")
    if a != e:
        raise ValueError("m_a and m_b can't be multiplied")
    alist = []
    blist = []
    for n in range(len(m_a)):
        for m in range(len(m_b[n])):
            c = 0
            for l in range(len(m_a[n])):
                c += m_a[n][l] * m_b[l][m]
            alist.append(c)
        blist.append(alist.copy())
        alist.clear()
    return blist
