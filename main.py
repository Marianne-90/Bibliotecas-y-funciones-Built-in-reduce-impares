from  functools import reduce


lista = [1,2,3,4,5,6,7]

listaFiltrada = list(filter(lambda x: x%2 ==1, lista))

listaFyReducida = reduce(lambda x,y : x+y, listaFiltrada)

print(f'la cantidad reducida es {listaFyReducida}')




