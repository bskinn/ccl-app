import dash
from dash import Dash, html as dhtml

app = Dash("ccl-app", use_pages=True)

HEADER_SECTION = "layout-header"
BODY_SECTION = "layout-body"

HEADER_HOME_LINK = "header-home-link"

app.layout = dhtml.Div(
    [
        dhtml.Div(
            id=HEADER_SECTION,
            children=[dhtml.A(id=HEADER_HOME_LINK, href="/", children="Home")],
        ),
        dhtml.Div(id=BODY_SECTION, children=dash.page_container),
    ]
)


if __name__ == "__main__":
    app.run_server()
