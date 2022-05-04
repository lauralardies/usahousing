# usahousing

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/usahousing)
https://github.com/lauralardies/usahousing

## Resumen: 
Para ver qué variables son las que más merecen la pena comparar, vamos a calcular su correlación lineal y la representaremos en una tabla. A partir de ahí, descartaremos determinadas variables y representaremos las variables que consideraremos oportunas a partir del estudio anterior.

## Correlación Lineal:
Una vez calculada y graficada la correlación lineal, podemos ver qué columnas son las que menos correlación aportan. Hemos aplicado el criterio de eliminar aquellas variables que tengan correlación menor o igual a 0,4. Acorde a este criterio, las columnas a eliminar son: "Avg. Area Number of Rooms" y "Avg. Area Number of Bedrooms". Entre ellas están ampliamente relacionadas, pero no vale la pena estudiarlas al tratarse de variables tan parecidas. Una es el número de habitaciones y la otra es el número de dormitorios, que es un tipo de habitación. A parte de la correlación entre ellas, no aportan mucha más información así que descartamos estas variables.

## Gráficas: 
Como último paso graficamos las variables restantes. Igualmente, hay que seguir teniendo en cuenta la correlación. Se puede observar que aquellas variables con mayor correlación siguen más la línea del gráfico. Sin embargo, aquellas que tienen menor correlación están agrupadas más en forma de "círculo" sin aportar mucha información. Para verificar lo que acabamos de decir, crearemos todas las gráficas posibles con los datos disponibles y las guardaremos en dos carpetas distintas en función de su correlación:
1) Carpeta "correlación": Aquí se guardan las gráficas que muestran correlación. Es decir, las dos variables dibujadas se influyen mutuamente.
2) Carpeta "no correlación":  Aquí se guardan las gráficas que no tienen tanta correlación. Es decir, las dos variables dibujadas son independienes (o casi).

Una vez ejecutado nuestro código podemos verificar nuestra teoría. Hemos observado que cuanta mayor correlación, menos tendencia hay a que se apelotonen los datos en forma de círculo, debido a que las variables dependen la una de la otra. Es decir, si sube una, la otra también. Como ejemplo práctico, esto ocurre en el caso de los ingresos de la zona al ser comparados con el precio de la casa. Cuanto más cara la casa, más ingresos gana su dueño y viceversa.

Con esto finalizamos nuestro análisis de datos.
