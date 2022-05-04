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