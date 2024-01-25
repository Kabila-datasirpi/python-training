import plotly.express as px
df=px.data.gapminder().query("country=='Canada'")
pic=px.bar(df,x="year", y="pop")
pic.show()

cf=px.data.medals_long()
fig=px.bar(cf,x="nation",y="count",color="medal")
fig.show()