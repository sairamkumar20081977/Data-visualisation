import pandas as pd
import plotly.express as ps
df=pd.read_csv("covid_data.csv")
fig=ps.line(df,x="date",y="cases",color="country",title="Covid Cases")
fig.show()