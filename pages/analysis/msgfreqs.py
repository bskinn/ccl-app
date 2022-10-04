r"""*Message posting frequency page for* ``ccl-app``.

``ccl-app`` is a multi-page Dash webapp providing tools
to explore the CCL mailing list corpus and explanation
of the functionality of the underlying tooling.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    13 Jul 2022

**Copyright**
    \(c) Brian Skinn 2022

**Source Repository**
    https://github.com/bskinn/ccl-app

**Documentation**
    *pending*

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

import calendar
from textwrap import dedent

import dash
import pandas as pd
import plotly.express as px
from dash import callback, dcc, html as dhtml
from dash.dependencies import Input, Output
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__)

load_figure_template("COSMO")


COL_COUNT = "count"
COL_DATE = "date"

HIGH_LEVEL_GRAPH = "msgfreqs-high-level-graph"
DETAILED_GRAPH = "msgfreqs-detailed-graph"
OPEN_DAY_ANCHOR = "msgfreqs-open-day-anchor"


def make_date_col(df: pd.DataFrame) -> pd.DataFrame:
    """Make a 'date' column from the data in the DataFrame.

    DataFrame must have at least a 'year' and 'month' column.

    If a 'day' column is present, it will be used; if absent,
    the first day of the month will be used.

    """
    if "day" not in df.columns:
        df = df.assign(day=[1] * len(df.index))

    return pd.to_datetime(df[["year", "month", "day"]])


def make_df(*, stem: str) -> pd.DataFrame:
    """Retrieve data and make DataFrame.

    Inserts the 'date' column after load.

    """
    df = pd.read_csv(f"data/{stem}.csv")
    return df.assign(date=make_date_col(df))


df_monthly = make_df(stem="monthly")
df_daily = make_df(stem="daily_w_zeroes")


def create_empty_graph():
    return px.scatter()


def create_high_level_graph():
    return px.bar(df_monthly, x="date", y="count")


def get_lowest_date_info(selected_data):
    """Supply year, month, day for the earliest date in selected_data.

    () --> tuple[Optional[int], Optional[int], Optional[int]]

    (year, month, day)

    selected_data is of the type returned by an `Input(..., "selectedData")`
    callback.

    """
    try:
        pts = selected_data["points"]
    except TypeError:  # selected_data is None
        return None, None, None

    if pts:
        d = min(p["x"] for p in pts)

        # Running the data points through `min` converts to yyyy-mm-dd strings
        return d.split("-")
    else:
        return None, None, None


layout = [
    dcc.Markdown(
        id="body-block-1",
        children=dedent(
            """
            # CCL.NET Message Posting Frequency

            Hover over a chart to show controls.

            Zoom (magnifying glass) and pan (up/down/left/right arrow) to the
            area of interest, then select a range of bars (dotted rectangle) to
            populate the posts-per-day chart below.

            ## Posts Per Month (Full Archive)

            """
        ),
    ),
    dcc.Graph(id=HIGH_LEVEL_GRAPH, figure=create_high_level_graph()),
    dcc.Markdown(
        id="body-block-2",
        children=dedent(
            """
            ## Posts Per Day (Selected Range)

            Use the same zoom/pan/select controls as above.

            After selecting some data, clicking the link below will take you to
            the day page on CCL for the first day in that range.

            """
        ),
    ),
    dhtml.Div(
        [
            dhtml.A("App loading...", id=OPEN_DAY_ANCHOR, target="_blank", href=""),
        ]
    ),
    dcc.Graph(id=DETAILED_GRAPH, figure=create_empty_graph()),
]


@callback(
    Output(DETAILED_GRAPH, "figure"),
    Input(HIGH_LEVEL_GRAPH, "selectedData"),
)
def set_detail_figure(hi_data):
    """Populate the detailed figure from the high-level selection."""
    try:
        pts = hi_data["points"]
    except TypeError:  # hi_data is None
        return create_empty_graph()

    if pts:
        min_date = min(p["x"] for p in hi_data["points"])
        max_date = max(p["x"] for p in hi_data["points"])

        # All months' dates are for the first day of the month.
        # We have to shift max_date to the last day of the month.
        md = pd.Timestamp(max_date)
        md = pd.Timestamp(
            year=md.year,
            month=md.month,
            day=calendar.monthrange(year=md.year, month=md.month)[1],
        )
        max_date = f"{md.year}-{md.month:0>2}-{md.day:0>2}"

    else:
        # Filters that return *no* data, so the chart will be blank
        # whenever no selection has been made
        min_date = pd.Timestamp(year=1990, month=12, day=1)
        max_date = pd.Timestamp(year=1990, month=12, day=31)

    df = df_daily[df_daily["date"] >= min_date]
    df = df[df["date"] <= max_date]

    return px.bar(df, x="date", y="count")


@callback(
    Output(OPEN_DAY_ANCHOR, "href"),
    Output(OPEN_DAY_ANCHOR, "children"),
    Input(DETAILED_GRAPH, "selectedData"),
)
def update_day_page_anchor(detail_data):
    """Update the link out to the CCL day page based on detail chart selection."""
    year, month, day = get_lowest_date_info(detail_data)

    if year:
        href = f"http://ccl.net/cgi-bin/ccl/day-index.cgi?{year}+{month:0>2}+{day:0>2}"
        text = f"Open {year}-{month:0>2}-{day:0>2} on CCL"
    else:
        href = "http://ccl.net/chemistry/resources/messages/index.shtml"
        text = dhtml.Em("(Nothing selected)")

    return href, text
