import dash
from dash import html
from flask_compress import Compress

dapp = dash.Dash(__name__)
dapp.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            children="Styling using html components",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        )
    ],
)

app = dapp.server
Compress(app)

if __name__ == "__main__":
    dapp.run_server()
