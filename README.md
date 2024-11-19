# Silly-Sorter
Silly sorter made by the TWENTY team.

## Descripción
Este programa interactivo en Python permite al usuario crear un diccionario de datos con claves y valores numéricos. Una vez creados, se pueden filtrar y ordenar los datos según diferentes condiciones. Es útil para explorar datos pequeños de manera rápida y organizada.

## Características
Recopilación de pares clave-valor.
Validación de entradas para asegurar que los valores sean numéricos.
Filtrado de datos con operadores comparativos (>, >=, <, <=).

## Cómo usar el programa
### Introduce los datos:

 1 Escribe una clave (cualquier texto).
 
 2 Introduce un valor numérico asociado.
 
 3 Repite el proceso para agregar más datos.
 
 4 Deja el campo de la clave vacío y presiona Enter para finalizar.

### Filtra los datos:

#### Especifica un operador de comparación:
##### >: Mayor que
##### >=: Mayor o igual que
##### <: Menor que
##### <=: Menor o igual que
#### Introduce un valor numérico como condición.
#### El programa mostrará los datos que cumplen la condición, ordenados según el operador.

### Resultado:
Los datos filtrados se mostrarán en un formato tabular junto con el tamaño del conjunto filtrado.

## Ejemplo
### Entrada:
Insert key: A
Insert value: 5
Insert key: B
Insert value: 10
Insert key: C
Insert value: 3
Insert key:

### Filtro:
Enter operation (>, >= or <, <=): >

Enter condition: 4

### Salida:

------------

A         :       5.0

B         :      10.0

------------

Size of filtered data: 2

Showing values > than 4

## Notas
Si introduces un valor no numérico, el programa mostrará un mensaje de error y pedirá que vuelvas a intentarlo.
Puedes reiniciar el proceso de filtrado en caso de cometer un error en la entrada.
