import pandas as pd
import plotly.express as ps
df=pd.read_csv("covid_data.csv")
fig=ps.bar(df,x="date",y="cases",title="Covid Cases")
fig.show()