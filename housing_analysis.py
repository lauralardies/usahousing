import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Para ver qué variables vamos a estudiar, calcularemos su correlación lineal y la representaremos en una gráfica.
# A parir de ahí representaremos las variables que consideraremos oportunas a partir del estudio anterior.

def correlacion(datos, n, saveas):
    correlation_matrix = datos.corr().round(n)
    sns.heatmap(data=correlation_matrix, annot=True)
    plt.savefig(("img/" + saveas + ".png"), bbox_inches = "tight")

def diagrama (var1, var2, saveas):

    plt.figure()
    sns.lmplot(x = var1, y = var2, data = df)
    plt.savefig(("img/" + saveas + ".png"))

df = pd.read_csv("USA_Housing.csv")

df_resumen = df.describe() # Esta función calcula la media, la desviación típica, el mínimo, máximo y los cuartiles de todos los datos de cada columna de nuestro archivo df.

correlacion(df, 1, "Antes") # Calculamos y graficamos la correlación lineal

# Descartamos las variables que tienen poca influencia, correlacion <= 0.4
df.pop("Avg. Area Number of Rooms")
df.pop("Avg. Area Number of Bedrooms")

correlacion(df, 2, "Después") # Calculamos y graficamos la nueva correlación lineal después que a ver eliminado las variables.

# Por lo tanto, sabemos que las gráficas que van a tener correlación son las siguientes: 

