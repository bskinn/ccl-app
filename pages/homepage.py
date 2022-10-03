from textwrap import dedent

import dash
from dash import dcc


dash.register_page(__name__, path="/")

layout = dcc.Markdown(
    id="home-temp-id",
    children=dedent(
        """\
    # CCL Information and Exploration App
    
    ## Information
    [Extracting Data from CCL Pages](/info/extract)
    
    ## Exploration/Analysis
    [Message Posting Frequencies](/analysis/msgfreqs)
    
    """
    ),
)
