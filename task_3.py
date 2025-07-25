import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.express as px


df = pd.read_csv("titanic.csv")
df["Sex"] = df["Sex"].map({"male": "Male", "female": "Female"})


app = dash.Dash(__name__)
app.title = "Titanic Dashboard"


fig1 = px.pie(df, names="Sex", values="Survived", title="Survival by Gender")


fig2 = px.bar(df, x="Pclass", y="Survived", color="Pclass", barmode="group", title="Survival by Class")


app.layout = html.Div(children=[
    html.H1("Titanic Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
    ]),

    html.H3("Passenger Table"),
    dash_table.DataTable(
        data=df[["Name", "Sex", "Age", "Survived"]].to_dict("records"),
        page_size=10,
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "left"}
    )
])

if __name__ == "__main__":
    app.run(debug=True)