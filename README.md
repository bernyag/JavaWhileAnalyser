# JavaWhileAnalyser

---
**Elaborado por:**
+ Bernardo Altamirano (167881)
+ Ivana Lucho (167028)
+ Andrea Padilla (166605)
+ América Castrejón (166414)
+ Alexis Calvillo (159702)
+ Maritrini García (151490)
---

## Introducción
El proyecto consiste en construir un sencillo reconocedor de enunciados while bien anidados en un lenguaje de programación. El programa debe leer los datos de entrada, un bloque de while's anidados sintácticamente correcto y debe arrojar como resultado la aceptación o rechazo del enunciado como correcto, y una serie de estadísticas relacionadas con las condiciones de prueba de cada while.

## Especificaciones generales

* El programa debe leer los datos de entrada de un archivo, al cual se le pasa por medio de la línea de comandos, o se le carga por medio de una ventana de dialogo de abrir archivo.
* El programa debe utilizar expresiones regulares para separar el flujo de datos de la entrada en tokens (Ejemplo: while, (, x, <, 5, ), {, while, }, etc.). Puedes usar los paquetes o bibliotecas estándar de expresiones regulares de Python o Java.
* Tu programa debe reconocer enunciados while bien anidados del lenguaje Java. Checa los ejemplos al final de esta especificación.
* Tu programa debe implementar un autómata de pila para parsear la entrada (divida en tokens de forma previa con expregs) y validar si en efecto se trata de un bloque de ciclos while bien anidados.
* NO SE PERMITE utilizar generadores de parseadores existentes, de ningun tipo y de ningun lenguaje. Si lo haces, tu proyecto automáticamente se evalua a 0.
* Cada enunciado while debe contener, por supuesto una expresión booleana entre paréntesis. Considera unicamente expresiones booleanas con las siguientes caracteristicas:
	* Variables de una sola letra ([a-z])
	* Constantes de un solo digito ([0-9])
	* Operadores relacionales: <, >, ==
* La salida del programa debe contener los siguientes datos:
	* Número total de variables (diferentes) usadas en todos los while encontrados.
	* Número total de operadores de comparación encontrados (con repeticiones).
	* Número total de while's que contiene el bloque parseado.
* El formato de la salida es a libre elección, pero debe ser claro.

## Funcionamiento
Para reconocer los whiles anidados, la solución se dividió en cinco módulos distintos:
* [Integrador](https://github.com/bernyag/JavaWhileAnalyser/blob/main/main.py)
Conecta los módulos y da la línea de entrada para los datos.

* [Tokenizador](https://github.com/bernyag/JavaWhileAnalyser/blob/main/tokenizador.py)
Recibe el texto en bruto y lo transforma a una lista de tokens usando expresiones regulares (no podemos usar paquetes predefinidos). Ej de lista saliente: [while,(,5,==,7,),{,}]

* [Léxico](https://github.com/bernyag/JavaWhileAnalyser/blob/main/automataPila.py)
Autómata de pila que determina si es un while bien formado o no. Su salida es un booleano.

* [Síntaxis](https://github.com/bernyag/JavaWhileAnalyser/blob/main/Sintax.py)
Revisa que las comparaciones sean válidas. Recibe la lista de tokens y su salida es un booleano.

* [Contador](https://github.com/bernyag/JavaWhileAnalyser/blob/main/contador.py)
Cuenta y da formato a la salida de variables, operadores y whiles. 

En este caso se utilizaron dos archivos de texto. En el caso del archivo [`input.txt`](https://github.com/bernyag/JavaWhileAnalyser/blob/main/input.txt) se incluye un enunciado while bien anidado; mientras que en alrchivo [`wrong.txt`](https://github.com/bernyag/JavaWhileAnalyser/blob/main/wrong.txt) el bloque no es sintácticamente correcto. El usuario puede modificar estos archivos para comprar el funcionamiento de la solución


## Ejecución
Para ejecutar el programa es necesario descargar el repositorio, contar con `Python` y colocarse sobre el archivo [`main.py`]() para correr cualquiera de los siguientes comandos en el CLI:
   
   `python3 main.py input.txt`

   `python3 main.py wrong.txt`
