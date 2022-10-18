#!/usr/bin/python3
'''
numpy
'''
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    '''
    using numpy to multiply a matrice
    '''
    x = np.arange(4, dtype=np.int64).reshape(2, 2)
    x = [[0, 0], [0, 0]]
    x[0][0] = m_a[0][0] * m_b[0][0] + m_a[0][1] * m_b[1][0]
    x[0][1] = m_a[0][0] * m_b[1][0] + m_a[0][1] * m_b[1][1]
    x[1][0] = m_a[1][0] * m_b[0][0] + m_a[0][1] * m_b[1][0]
    x[1][1] = m_a[1][0] * m_b[1][0] + m_a[0][1] * m_b[1][1]
