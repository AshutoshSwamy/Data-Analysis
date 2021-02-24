import pandas as pd
import plotly.express as px

df = pd.read_csv("data_2.csv")
fig = px.bar(df, x = "Discoverer" , y = "Chemical Element Name", title = "Discorver Comparison Of Chemical Elements")
fig.show()