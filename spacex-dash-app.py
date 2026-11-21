
# ==========================================================
# SPACEX LAUNCH RECORDS DASHBOARD
# IBM Data Science Project
# ==========================================================

# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px


# ==========================================================
# STEP 1: READ THE DATASET
# ==========================================================

# Read the SpaceX launch data into Pandas DataFrame
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Find minimum and maximum payload values
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()


# ==========================================================
# STEP 2: CREATE DASH APPLICATION
# ==========================================================

app = dash.Dash(__name__)


# ==========================================================
# STEP 3: CREATE APPLICATION LAYOUT
# ==========================================================

app.layout = html.Div(children=[

    # Dashboard Heading
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': 40
        }
    ),

    html.Br(),

    # ------------------------------------------------------
    # TASK 1: LAUNCH SITE DROPDOWN
    # ------------------------------------------------------

    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'}
        ] + [
            {'label': site, 'value': site}
            for site in spacex_df['Launch Site'].unique()
        ],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),

    html.Br(),

    # ------------------------------------------------------
    # TASK 2: PIE CHART COMPONENT
    # ------------------------------------------------------

    html.Div(
        dcc.Graph(id='success-pie-chart')
    ),

    html.Br(),

    # Payload Range Heading
    html.P("Payload range (Kg):"),

    # ------------------------------------------------------
    # TASK 3: PAYLOAD RANGE SLIDER
    # ------------------------------------------------------

    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={
            0: '0',
            1000: '1000',
            2000: '2000',
            3000: '3000',
            4000: '4000',
            5000: '5000',
            6000: '6000',
            7000: '7000',
            8000: '8000',
            9000: '9000',
            10000: '10000'
        },
        value=[min_payload, max_payload]
    ),

    html.Br(),

    # ------------------------------------------------------
    # TASK 4: SCATTER CHART COMPONENT
    # ------------------------------------------------------

    html.Div(
        dcc.Graph(id='success-payload-scatter-chart')
    )

])


# ==========================================================
# STEP 4: TASK 2 - PIE CHART CALLBACK
# ==========================================================

@app.callback(
    Output(
        component_id='success-pie-chart',
        component_property='figure'
    ),
    Input(
        component_id='site-dropdown',
        component_property='value'
    )
)

def get_pie_chart(entered_site):

    # Check whether ALL sites are selected
    if entered_site == 'ALL':

        # Show successful launches for all launch sites
        fig = px.pie(
            spacex_df[spacex_df['class'] == 1],
            names='Launch Site',
            title='Total Successful Launches by Launch Site'
        )

    else:

        # Filter data for the selected launch site
        filtered_df = spacex_df[
            spacex_df['Launch Site'] == entered_site
        ]

        # Show successful and failed launches
        fig = px.pie(
            filtered_df,
            names='class',
            title='Success vs Failure for ' + entered_site
        )

    return fig


# ==========================================================
# STEP 5: TASK 4 - SCATTER PLOT CALLBACK
# ==========================================================

@app.callback(
    Output(
        component_id='success-payload-scatter-chart',
        component_property='figure'
    ),
    [
        Input(
            component_id='site-dropdown',
            component_property='value'
        ),
        Input(
            component_id='payload-slider',
            component_property='value'
        )
    ]
)

def get_scatter_chart(entered_site, payload_range):

    # Get minimum and maximum selected payload values
    low, high = payload_range

    # Check whether ALL sites are selected
    if entered_site == 'ALL':

        # Filter records based on payload range
        filtered_df = spacex_df[
            (spacex_df['Payload Mass (kg)'] >= low) &
            (spacex_df['Payload Mass (kg)'] <= high)
        ]

    else:

        # Filter records based on launch site and payload range
        filtered_df = spacex_df[
            (spacex_df['Launch Site'] == entered_site) &
            (spacex_df['Payload Mass (kg)'] >= low) &
            (spacex_df['Payload Mass (kg)'] <= high)
        ]

    # Create scatter plot
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload Mass vs Launch Success',
        labels={
            'Payload Mass (kg)': 'Payload Mass (Kg)',
            'class': 'Launch Outcome',
            'Booster Version Category': 'Booster Version'
        }
    )

    return fig


# ==========================================================
# STEP 6: RUN THE DASH APPLICATION
# ==========================================================

if __name__ == '__main__':
    app.run(debug=True)
