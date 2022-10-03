import dash
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt
from dash import Dash, html as dhtml

dbt.load_figure_template("cosmo")

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.COSMO])


HEADER_SECTION = "layout-header"
BODY_SECTION = "layout-body"

HEADER_HOME_LINK = "header-home-link"


app.layout = dhtml.Div(
    [
        dhtml.Div(
            id=HEADER_SECTION,
            children=[
                dhtml.A(
                    id=HEADER_HOME_LINK,
                    href="/",
                    children="Home",
                )
            ],
        ),
        dhtml.Div(id=BODY_SECTION, children=dash.page_container),
    ],
)


if __name__ == "__main__":
    app.run_server()
