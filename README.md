# Proyecto ETL III

El proyecto de esta semana consiste en hacer el proceso completo de ETL: extracción, transformación y carga.

Hemos elegido extraer información relacionada con  subastas de viviendas en España. Posteriormente lo analizaremos por provincias comparándolas también por el coste del metro cuadrado.



## Requisitos:

1. Extraer datos de tres fuentes diferentes y utilizar mínimo 2 métodos de extracción.

2. Transformación de los datos. (Crear y limpiar tablas, ER...)

3. Guardar las tablas en alguna base de datos. (MySQL, Mongo)


## Proceso

Empezaremos escrapeando algunas páginas webs;

El primer reto que nos encontramos es descifrar la estructura de cada URL para realizar busquedas directas y copiar el XPATH de cada tabla que nos interesa. 

Una vez descifrada la URL que más nos compensa, empezamos el scrapeo:

Empezamos a scrapear los primeros datos, que serán del BOE donde sacaremos dos tablas, que limpiaremos detalladamente. 
Mas adelante utilizaremos MySQL como alojamiento de esos datos.

Tambien scrapeamos de la pagina oficial de bankinter los datos relaciones con el coste del m2 por provincia del 2022. Esa informacion la relacionaremos con las tablas anteriores para sacar conclusiones.

Por ahora hemos utilziado solamente una forma de extraccion de datos. A continuacion descargamos dos archivos csv y los abrimos en python donde limpairemos también las columnas.

Las fuentes de estos datos serán del INE.

Una vez lo tenemos limpiado, procedemos a  añadir nuevas columnas con su id  para poder relacionar cada tabla.  

Finalmente exportamos los datos a MySQL para analizarlos con mayor detalle

