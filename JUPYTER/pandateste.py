import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/brunamulinari/BasicPythonProjects/main/Base_ficticia/baseficticia.csv', sep = ';')

type(df) 

df.head(n=6)