import pandas as pd
import plotly.express as px

df = pd.read_csv("data_3.csv")
fig = px.pie(df, values = "Runs Scored", names = "Player Name", color = "Balls Played", title = "Performance Of Indian Batsmen In IND v AUS 2nd ODI")
fig.show()