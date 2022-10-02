import dash
from dash import Dash, html as dhtml

external_scripts = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = Dash("ccl-app", use_pages=True, external_scripts=external_scripts)

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
                    className="text-blue-700 visited:text-purple-700 hover:bg-gray-200",
                )  # TODO: Refactor project into package and add module with classNames
            ],
            className="pb-4",
        ),
        dhtml.Div(id=BODY_SECTION, children=dash.page_container),
    ],
    className="p-4",
)


if __name__ == "__main__":
    app.run_server()
