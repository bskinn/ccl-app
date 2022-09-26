import dash
from dash import Dash, html as dhtml

app = Dash("ccl-app", use_pages=True)

app.layout = dhtml.Div([dash.page_container])

if __name__ == "__main__":
    app.run_server()
