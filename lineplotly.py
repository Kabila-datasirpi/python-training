import plotly.express as px
df=px.data.gapminder().query("country=='Canada'")
pic=px.line(df, x="year", y="lifeExp", title="lifeexpentance in canada",)
pic.show()


cg=px.data.gapminder().query("continent=='Oceania'")
p=px.line(cg, x="year",y="lifeExp", color="country",markers="true")
p.show()