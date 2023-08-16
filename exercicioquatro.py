import math
import numpy as np
import numpy.random as npr

#Gere um quinto ndarray de inteiros aleatórios de uma dimensão 
#utilizando o método de sua preferência da biblioteca NumPy Random
nd5 = npr.randint(0,10,10)

#Gere um sexto ndarray de inteiros aleatórios de uma dimensão 
#utilizando o método de sua preferência da biblioteca NumPy Random
nd6 = npr.randint(0,10,10)

print(nd5)
print(nd6)

# Imprima no console todos os elementos comuns do 
# quinto e do sexto ndarrays
i = 0
while i < 10:
    if nd5[i] == nd6[i]: 
        print(nd5[i])
    i = i + 1

# Imprima no console os índices de todos os elementos comuns do
# quinto e do sexto ndarrays
indice = np.arange(True * 10)
i = 0
while i < 10:
    if nd5[i] == nd6[i]: 
        indice[i] = True
    else: indice[i] = False
    i = i + 1
    
print("indices: ", indice)

# Imprima no console todos os elementos do quinto ndarray que não 
# são elementos do sexto ndarray
i = 0
while i < 10:
    if indice[i] == False:
        print(nd5[i])
    i = i + 1