"""Main menu dashboard for CCL-APP."""

import plotly.express as px
from dash import Dash, dcc, html as dhtml
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from ccl_app.msgfreqs.app import app as app_msgfreqs

app_main = Dash("ccl-app-main")
app_main.layout = dcc.Markdown(
  id="main-markdown",
  children="""
  [msgfreqs](/msgfreqs)
  """
)

app_dispatcher = DispatcherMiddleware(app_main.server, mounts={
    "/msgfreqs": app_msgfreqs.server,
})


if __name__ == "__main__":
    app_dispatcher.run() 

    