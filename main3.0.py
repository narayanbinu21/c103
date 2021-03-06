import pandas as pd
import plotly.express as px

df = pd.read_csv("line_chart.csv")
fig = px.scatter(df,x="Year", y="Per capita income", color = "Country",size_max=60)
fig.show()