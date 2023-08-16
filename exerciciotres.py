import numpy as np

def dever_rafael():
    rafael = np.arange(1, 11)
    rafaell = np.arange(11, 21)
    soma_elementos = rafael + rafaell

    print("rafael:", rafael)
    print("rafaell:", rafaell)
    print("Soma Elemento a Elemento:", soma_elementos)

    array_naosei = np.random.randint(1, 31, size=(10))

    print("Array Não Sei:")
    print(array_naosei)

    resultado_multiplicacao = soma_elementos * array_naosei

    array_naosei = resultado_multiplicacao

    print("\nResultado da Multiplicação:")
    print(resultado_multiplicacao)
    print("\nArray Não Sei Atualizado:")
    print(array_naosei)

dever_rafael()
