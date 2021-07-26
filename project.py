import pandas as pd 
import plotly.express as px
import csv

df = pd.read_csv("data1.csv")
a=df.groupby(["level","student_id"],as_index=False)["attempt"].mean()

fig = px.scatter(a, y="level", x="student_id", color="attempt", size="attempt")
fig.show()