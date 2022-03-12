#Ejercicio 16.4. Ordenar la lista 6 0 3 2 5 7 4 1 usando el método quicksort. Mostrar el árbol de recursividad explicando las llamadas que se hacen en cada paso, y el orden en el que se realizan.

                                    6 0 3 2 5 7 4 1
                                        pivote=6
                                        menores=0 3 2 5 4 1
                                        mayores= 7

       quicksort(mayores)==>7                                quicksort(menores)==> 
                                                   pivote=0,menores=[], mayores=3 2 5 4 1
                                                 quicksort(menores)        quicksort(mayores)
                                                        []                      pivote=3
                                                                                menores=2 1
                                                                                mayores=5 4

                                                                 quicksort(menores) quicksort(mayores)
                                                                 pivote=2               pivote=5
                                                                 menores=1              menores=4
                                                                 mayores=[]             mayores=[]


                                                                    12                         45

                                                                               12 3 45

                                                                              0 12345

                                        012345 6 7




