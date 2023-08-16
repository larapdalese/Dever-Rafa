import numpy as np

def calcular_estatisticas():
    quinto_ndarray = np.random.randint(1, 11, size=20)
    sexto_ndarray = np.random.randint(11, 21, size=20)

    setimo_ndarray = np.hstack((quinto_ndarray, sexto_ndarray))

    print("Quinto ndarray:", quinto_ndarray)
    print("Sexto ndarray:", sexto_ndarray)
    print("\nSétimo ndarray (Empilhamento Horizontal):")
    print(setimo_ndarray)

    media = np.mean(setimo_ndarray)
    desvio_padrao = np.std(setimo_ndarray)
    variancia = np.var(setimo_ndarray)

    print("\nMédia:", media)
    print("Desvio Padrão:", desvio_padrao)
    print("Variância:", variancia)

calcular_estatisticas()
