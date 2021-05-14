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
El proyecto consiste en construir un sencillo reconocedor de enunciados while bien anidados de un lenguaje de programación. El programa debe leer los datos de entrada, un bloque de while's anidados sintacticamente correcto y debe arrojar como resultado la aceptacion o rechazo del enunciado como correcto y una serie de estadisticas relacionadas con las condiciones de prueba de cada while.

## Especificaciones generales

* El programa debe leer los datos de entrada de un archivo, el cual se le pasa por medio de la línea de comandos o se carga por medio de una ventana de dialogo de abrir archivo.
* El programa debe utilizar expresiones regulares para separar el flujo de datos de la entrada en tokens (Ejemplo: while, (, x, <, 5, ), {, while, }, etc.). Puedes usar los paquetes o bibliotecas estándar de expresiones regulares de Python o Java.
* Tu programa debe reconocer enunciados while bien anidados del lenguaje Java. Checa los ejemplos al final de esta especificacion.
* Tu programa debe implementar un automata de pila para parsear la entrada (divida en tokens de forma previa con expregs) y validar si en efecto se trata de un bloque de ciclos while bien anidados.
* NO SE PERMITE utilizar generadores de parseadores existentes, de ningun tipo y de ningun lenguaje. Si lo haces, tu proyecto automaticamente se evalua a 0.
* Cada enunciado while debe contener, por supuesto una expresion booleana entre parentesis. Considera unicamente expresiones booleanas con las siguientes caracteristicas:
	* Variables de una sola letra ([a-z])
	* Constantes de un solo digito ([0-9])
	* Operadores relacionales: <, >, ==
* La salida del programa debe contener los siguientes datos:
	* Numero total de variables (diferentes) usadas en todos los while encontrados.
	* Numero total de operadores de comparacion encontrados (con repeticiones).
	* Numero total de while's que contiene el bloque parseado.
* El formato de la salida es a libre elección, pero debe ser claro.

## Funcionamiento
Para reconocer los whiles anidados se definió la arquitectura que se muestra en la siguiente figura. La solución se dividió en cinco módulos distintos:
* [Integrador]()
Conectar los módulos y da la línea de entrada para los datos.

* [Tokenizador]()
Recibe el texto en bruto y lo transforma a una lista de tokens usando expresiones regulares (no podemos usar paquetes predefinidos). Ej de lista saliente: [while,(,5,==,7,),{,}]

* [Léxico]()
Autómata de pila que determina si es un while bien formado o no. Su salida es un booleano.

* [Síntaxis]()
Revisa que las comparaciones sean válidas. Recibe la lista de tokens y su salida es un booleano.

* [Contador]()
Cuenta y da formato a la salida de variables, operadores y whiles. 

En este caso se utilizaron dos archivos de textos. En el caso del archivo [`input.txt`]() se incluye un enunciado while bien anidados; mientras que en alrchivo [`wrong.txt`]() el bloque no es sintacticamente correcto. El usuario puede modificar estos archivos para comprar el funcionamiento de la solución


## Ejecución
Para ejecutar el programa es necesario descargar el repositorio, contar con `Python` y colocarse sobre el archivo [`main.py`]() para correr cualquiera de los siguientes comandos en el CLI:
   
   `python3 main.py input.txt`

   `python3 main.py wrong.txt`