from textwrap import dedent

import dash
from dash import callback, Dash, dcc, html as dhtml


dash.register_page(__name__, path="/")

layout = dcc.Markdown(
    id="home-temp-id",
    children=dedent(
        """\
    # CCL Information and Exploration App
    
    ## Information
    *Information page links will go here at some point.*
    
    ## Exploration/Analysis
    [Message Posting Frequencies](/msgfreqs)
    
    """
    ),
)
