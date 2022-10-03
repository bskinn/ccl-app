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
        children="""\
            # Extracting Data From CCL Pages
            
            This is a first block of Markdown.
            
            ***IT CAN BE FORMATTED!***
            
            This is a very long block of text that is being written to test just how wide
            the rendering actually is for a block of Markdown. Partly, this is a test
            to see how wide the rendering is going, to see if there's something
            capping the width of the input box below, or if that's just something
            I'll need to adjust in the config for that input control.
            
            Yup. Need to change its width directly, looks like.
            
            Enter a sender info chunk:
            
            """,
    ),
    dcc.Input(id=INPUT_SENDER_INFO, value="John Doe (jdoe^^example.com)",
              size="40", debounce=True),
    dhtml.Br(),
    dhtml.Button(id=BTN_EXTRACT_SENDER_INFO, children="Extract Name/Email"),
    dhtml.Br(),
    dhtml.Br(),
    dhtml.Div(
        [
            dhtml.Span("Name: "),
            dhtml.Span(id=OUTPUT_SENDER_NAME, children="John Doe"),
            dhtml.Br(),
            dhtml.Span("Email: "),
            dhtml.Span(id=OUTPUT_SENDER_EMAIL, children="jdoe^^example.com"),
            dhtml.Br(),
            dhtml.Br(),
        ]
    ),
    dcc.Markdown(
        id="body-block-2",
        children="""\
            This is a second block of Markdown.
            """,
    ),
]


@callback(
    Output(OUTPUT_SENDER_NAME, "children"),
    Input(BTN_EXTRACT_SENDER_INFO, "n_clicks"),
    Input(INPUT_SENDER_INFO, "n_submit"),
    State(INPUT_SENDER_INFO, "value")
)
def process_btn_extract_for_name(btn_clicks, input_submits, input_value):
    _, name = extract_name_and_munged_email(input_value)
    return name

@callback(
    Output(OUTPUT_SENDER_EMAIL, "children"),
    Input(BTN_EXTRACT_SENDER_INFO, "n_clicks"),
    Input(INPUT_SENDER_INFO, "n_submit"),
    State(INPUT_SENDER_INFO, "value")
)
def process_btn_extract_for_name(btn_clicks, input_submits, input_value):
    email, _ = extract_name_and_munged_email(input_value)
    return email
