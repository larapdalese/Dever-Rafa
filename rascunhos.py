import numpy as np

#aqui nós geramos os valores, usamos o "np.arange para gera valores dentro 
##do intervalo decidido, 1-10 e de 10-20
rafael = np.arange(1, 11)
rafaell = np.arange(11, 21)

# aqui nós pedimos para somar esses dois arrays
soma_elementos = rafael + rafaell

print("rafael:", rafael)
print("rafaell", rafaell)
print("Soma Elemento a Elemento:", soma_elementos)
