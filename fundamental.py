import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

values = dcc.RadioItems(
    options=[
        {"label": x, "value": x}
        for x in [-640, -320, -160, -80, -60, -40, -20, 20, 40, 60, 80, 160, 320, 640]
    ],
    id="winning",
    # value=20,
    labelStyle={"display": "block"},
)

people = dcc.RadioItems(
    options=[{"label": x, "value": x} for x in ["AXW", "ANYQ", "ETJK", "GHR"]],
    # value="AXW",
    id="winner",
    labelStyle={"display": "block"},
)


df = pd.DataFrame(columns=["Name", "Amount"])


fig = go.Figure(
    go.Indicator(value=df["Amount"].sum(), number={"font": {"size": 64}}),
)

fig.update_layout(height=200)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div("AXW"),
                        dcc.Graph(figure=fig, id="AXW_OUTPUT"),
                    ],
                    className="three columns",
                ),
                html.Div(
                    [
                        html.Div("ANYQ"),
                        dcc.Graph(figure=fig, id="ANYQ_OUTPUT"),
                    ],
                    className="three columns",
                ),
                html.Div(
                    [
                        html.Div("ETJK"),
                        dcc.Graph(figure=fig, id="ETJK_OUTPUT"),
                    ],
                    className="three columns",
                ),
                html.Div(
                    [
                        html.Div("GHR"),
                        dcc.Graph(figure=fig, id="GHR_OUTPUT"),
                    ],
                    className="three columns",
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                html.Div(values, className="four columns", style={"font-size": "24px"}),
                html.Div(people, className="four columns", style={"font-size": "24px"}),
                html.Div(
                    html.Button("SUBMIT", id="button", style={"font-size": "24px"})
                ),
            ],
            className="row",
        ),
    ]
)


@app.callback(
    Output(component_id="AXW_OUTPUT", component_property="figure"),
    Output(component_id="ANYQ_OUTPUT", component_property="figure"),
    Output(component_id="ETJK_OUTPUT", component_property="figure"),
    Output(component_id="GHR_OUTPUT", component_property="figure"),
    Input("button", "n_clicks"),
    State(component_id="winning", component_property="value"),
    State(component_id="winner", component_property="value"),
)
def update_output_div(n_clicks, winning, winner):

    global df
    df_2 = pd.DataFrame({"Name": [winner], "Amount": int(winning)})

    df = pd.concat([df, df_2])

    print(df)

    XW = go.Figure(
        go.Indicator(
            value=int(df[df["Name"] == "AXW"]["Amount"].sum()),
            number={"font": {"size": 64}},
        )
    )
    AN = go.Figure(
        go.Indicator(
            value=int(df[df["Name"] == "ANYQ"]["Amount"].sum()),
            number={"font": {"size": 64}},
        )
    )
    ET = go.Figure(
        go.Indicator(
            value=int(df[df["Name"] == "ETJK"]["Amount"].sum()),
            number={"font": {"size": 64}},
        )
    )
    HR = go.Figure(
        go.Indicator(
            value=int(df[df["Name"] == "GHR"]["Amount"].sum()),
            number={"font": {"size": 64}},
        )
    )

    return XW, AN, ET, HR


if __name__ == "__main__":
    app.run_server(debug=True)