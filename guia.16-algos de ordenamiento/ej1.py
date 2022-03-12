#Ejercicio 16.1. Mostrar los pasos del ordenamiento de la lista 0 9 3 8 5 3 2 4 con los algoritmos de inserción y selección

con algoritmo de seleccion:

1. 0 9 3 8 5 3 2 4
2. 0 2 3 8 5 3 9 4
3. 0 2 3 9 8 5 3 4
4. 0 2 3 3 8 5 9 4
5. 0 2 3 3 4 5 9 8
6. 0 2 3 3 4 5 9 8
7. 0 2 3 3 4 5 8 9

con algoritmo de inserción:

1. 0 9 3 8 5 3 2 4   i=1, v=9, j=0, l[0]=0 ==> l[1]=9
2. 0 9 3 8 5 3 2 4   i=2, v=3, j=1, l[1]=9 ==> l[2]=9, j=0 ==> l[1]=3
3. 0 3 9 8 5 3 2 4   i=3, v=8, j=2, l[2]=9 ==> l[3]=9, j=1 ==> l[2]=8
4. 0 3 8 9 5 3 2 4   i=4, v=5, j=3, l[3]=9 ==> l[4]=9, j=2 ==> l[3]=8, j=1 ==>l[2]=5
5. 0 3 5 8 9 3 2 4  
...




