# usahousing

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/usahousing)
https://github.com/lauralardies/usahousing

## Resumen
Para ver qué variables son las que más merecen la pena comparar, vamos a calcular su correlación y la representaremos en una tabla. A partir de ahí, descartaremos determinadas variables y representaremos las variables que consideraremos oportunas a partir del estudio anterior.

## Correlación
Una vez calculada y graficada la correlación, podemos ver qué columnas son las que menos correlación aportan. Hemos aplicado el criterio de eliminar aquellas variables que tengan correlación menor o igual a 0,4. Acorde a este criterio, las columnas a eliminar son: "Avg. Area Number of Rooms" y "Avg. Area Number of Bedrooms". Entre ellas están ampliamente relacionadas, pero no vale la pena estudiarlas al tratarse de variables tan parecidas. Una es el número de habitaciones y la otra es el número de dormitorios, que es un tipo de habitación. A parte de la correlación entre ellas, no aportan mucha más información así que descartamos estas variables.

## Gráficas
Como último paso graficamos las variables restantes. Igualmente, hay que seguir teniendo en cuenta la correlación. Se puede observar que aquellas variables con mayor correlación siguen más la línea del gráfico. Sin embargo, aquellas que tienen menor correlación están agrupadas más en forma de "círculo" sin aportar mucha información. Para verificar lo que acabamos de decir, crearemos todas las gráficas posibles con los datos disponibles y las guardaremos en dos carpetas distintas en función de su correlación:
1) Carpeta "correlación": Aquí se guardan las gráficas que muestran correlación. Es decir, las dos variables dibujadas se influyen mutuamente.
2) Carpeta "no correlación":  Aquí se guardan las gráficas que no tienen tanta correlación. Es decir, las dos variables dibujadas son independienes (o casi).

Una vez ejecutado nuestro código podemos verificar nuestra teoría. Hemos observado que cuanta mayor correlación, menos tendencia hay a que se apelotonen los datos en forma de círculo, debido a que las variables dependen la una de la otra. Es decir, si sube una, la otra también. De igual manera, se puede decir lo contrario. Cuanto menor correlación, se puede observar que en nuestra gráfica los datos tienen mayor tendencia a juntarse sin aportar nada de información al intentar analizar la gráfica. Como ejemplo práctico, esto ocurre en el caso de los ingresos de la zona al ser comparados con el precio de la casa, que están altamente correlacionados. Cuanto más cara la casa, más ingresos gana su dueño y viceversa. Por otro lado, cuando comparamos la población de la zona con la edad de la casa (datos con baja correlación), podemos obervar que el hecho de que haya más población en la zona no influye en absoluto en la edad de la casa. Ambas variables no dependen la una de la otra, es decir, si una sube su valor, la otra no tiene porqué subir el suyo necesariamente.



Con esto finalizamos nuestro análisis de datos.



## Código
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------
# ¡ANÁLISIS COMPLETO EN EL READ ME!
# ---------------------------------

def correlacion(datos, n, saveas):
    correlation_matrix = datos.corr().round(n)
    sns.heatmap(data=correlation_matrix, annot=True)
    plt.savefig(("img/" + saveas + ".png"), bbox_inches = "tight")

def diagrama (var1, var2, correlacion, saveas):

    plt.figure()
    sns.lmplot(x = var1, y = var2, data = df)
    plt.savefig(("img/" + correlacion + "/" + saveas + ".png"))

df = pd.read_csv("USA_Housing.csv") # Creamos nuestro Dataframe con la ayuda de pandas.

correlacion(df, 1, "Antes") # Calculamos y graficamos la correlación lineal.

# Descartamos las variables que tienen poca influencia, correlacion <= 0,4.
df.pop("Avg. Area Number of Rooms")
df.pop("Avg. Area Number of Bedrooms")

correlacion(df, 2, "Después") # Calculamos y graficamos la nueva correlación lineal después de haber eliminado las variables.

# CORRELACIÓN. 

# 1 - Ingresos - Precio.
diagrama("Avg. Area Income", "Price", "correlación", "Ingresos - Precio")

# 2 - Edad Casa - Precio.
diagrama("Avg. Area House Age", "Price", "correlación", "Edad Casa - Precio")

# 3 - Población - Precio.
diagrama("Area Population", "Price", "correlación", "Población- Precio")

# NO CORRELACIÓN. 

# 1 - Edad Casa - Ingresos.
diagrama("Avg. Area House Age", "Avg. Area Income", "no correlación", "Edad Casa - Ingresos")

# 2 - Edad Casa - Población.
diagrama("Avg. Area House Age", "Area Population", "no correlación", "Edad Casa - Población")

# 3 - Ingresos - Población.
diagrama("Avg. Area Income", "Area Population", "no correlación", "Ingresos - Población")
```
