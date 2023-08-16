import math
import numpy as np
import numpy.random as npr

# Gere dois ndarrays de inteiros de uma dimensão utilizando o método de sua preferência da biblioteca NumPy
nd1 = np.arange(10)
nd2 = np.arange(10,20)
# Atribua a um terceiro ndarray a soma elemento a elemento dos dois primeiros ndarrays
nd3 = nd1 + nd2
############################

# Redimensione o terceiro ndarray para duas dimensões
nd3.shape = (2, 5)
print("Terceiro ndarray com duas dimensões: \n", nd3)

# Converta os dados para algum tipo de ponto flutuante
nd3 = nd3.astype(float)
print("Dados convertidos para ponto flutuante: \n", nd3)

# Atribua ao terceiro ndarray sua transposta
nd3 = np.transpose(nd3)
print("Transposta atribuida ao terceiro array: \n", nd3)