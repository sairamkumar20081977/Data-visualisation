import pandas as pd
import plotly.express as ps
df=pd.read_csv("covid_data.csv")
fig=ps.scatter(df,x="date",y="cases",color="country",title="Covid Cases",size_max=60)
fig.show()