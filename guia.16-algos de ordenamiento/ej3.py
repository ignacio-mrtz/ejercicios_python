#Ejercicio 16.3. Mostrar los pasos del ordenamiento de la lista: 6 0 3 2 5 7 4 1 con los métodos de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál usarías en qué casos?

l= 6 0 3 2 5 7 4 1

con metodo de inserción:

l= 6 0 3 2 5 7 4 1
l= 0 6 3 2 5 7 4 1
l= 0 3 6 2 5 7 4 1
l= 0 2 3 6 5 7 4 1
l= 0 2 3 5 6 7 4 1
l= 0 2 3 5 6 7 4 1
l= 0 2 3 4 5 6 7 1
l= 0 1 2 3 4 5 6 7

con metodo mergesort:

                                        l= 6 0 3 2 5 7 4 1
                            6 0 3 2                             5 7 4 1
                     6 0               3 2                 5 7            4 1
                  6      0           3     2            5      7     4         1
                     06                 23                 57             14
                             0236                                 1457
                                             01234567
                            


inserción se elige cuando se sabe que la lista esta casi ordenada y cuando es corta

mergesort es muyu predecible(sabes que siempre el tiempo qu tarda es o(nlogn)) pero no se puede implementar in-place