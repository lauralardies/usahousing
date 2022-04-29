import pandas as pd
import numpy as np 

df = pd.read_csv("USA_Housing.csv")

df_resumen = df.describe()
print(df_resumen)