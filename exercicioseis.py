'''
Defina dois vetores, A e B
Imprima no console o produto vetorial AxB
'''

import numpy as np

def produto_vetorial():
    A = [1, 2]
    B = [3, 4]
    print(np.cross(A, B))

produto_vetorial()