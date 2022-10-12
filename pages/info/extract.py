from textwrap import dedent

import dash
from ccl_db.ccl.extract import extract_name_and_munged_email
from dash import callback, dcc, html as dhtml
from dash.dependencies import Input, Output, State

dash.register_page(__name__)

INPUT_SENDER_INFO = "input-sender-info"
BTN_EXTRACT_SENDER_INFO = "btn-extract-sender-info"
OUTPUT_SENDER_NAME = "output-sender-name"
OUTPUT_SENDER_EMAIL = "output-sender-email"

layout = [
    dcc.Markdown(
        id="body-block-1",
        children=dedent(
            """
            # Extracting Data From CCL Pages

            The first step in storing messages from CCL into a database is
            scraping them from the CCL website itself.

            This page describes the layout of the content on `ccl.net` itself,
            and the methods used to scrape and extract that content into the
            individual fields stored in the SQLite database.

            ## Processing of Incoming Data

            When a message is processed by the CCL server, it parses the header
            and body, extracts a number of things, munges anything the the
            header or body that looks like an email address, and then (i) queues
            the email-munged message for distribution to the list, and (ii)
            creates items/pages in the List Archive section of the site to
            display the message publicly.

            ## Layout of Content on `ccl.net`

            ...

            ----

            Enter a sender info chunk:

            """
        ),
    ),
    dcc.Input(
        id=INPUT_SENDER_INFO,
        value="John Doe (jdoe^^example.com)",
        size="40",
        debounce=True,
    ),
    dhtml.Br(),
    dhtml.Button(id=BTN_EXTRACT_SENDER_INFO, children="Extract Name/Email"),
    dhtml.Br(),
    dhtml.Br(),
    dhtml.Div(
        [
            dhtml.Span(dhtml.B("Name: ")),
            dhtml.Span(id=OUTPUT_SENDER_NAME, children="John Doe"),
            dhtml.Br(),
            dhtml.Span(dhtml.B("Email: ")),
            dhtml.Span(id=OUTPUT_SENDER_EMAIL, children="jdoe^^example.com"),
            dhtml.Br(),
            dhtml.Br(),
        ]
    ),
    dcc.Markdown(
        id="body-block-2",
        children=dedent(
            """
            *This is a second block of Markdown.*
            """
        ),
    ),
]


@callback(
    Output(OUTPUT_SENDER_EMAIL, "children"),
    Output(OUTPUT_SENDER_NAME, "children"),
    Input(BTN_EXTRACT_SENDER_INFO, "n_clicks"),
    Input(INPUT_SENDER_INFO, "n_submit"),
    State(INPUT_SENDER_INFO, "value"),
)
def process_btn_extract_for_name(btn_clicks, input_submits, input_value):
    return extract_name_and_munged_email(input_value)
