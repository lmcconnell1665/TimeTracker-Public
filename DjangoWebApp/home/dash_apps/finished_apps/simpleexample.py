import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
import os
import datetime as dt
import numpy as np

app = DjangoDash('SimpleExample')

app.css.append_css({'external_url': '/static/css/sb-admin-2.css'})

os.chdir('/Users/lukemcconnell/Desktop/dev/TimeTracker/')
data = pd.read_csv('fct_entries.csv')

data['duration'] = pd.to_timedelta(data['duration'])
data['date'] = pd.to_datetime(data['startTime'].values).strftime('%a, %b %d %Y')

data_clean = data.groupby(['date'], as_index=False).agg({'duration': np.sum, 'polarity': np.sum})

data_clean['date'] = pd.to_datetime(data_clean['date'])
data_clean['duration'] = pd.to_timedelta(data_clean['duration'])

data_clean = data_clean.sort_values(by='date')

app.layout = html.Div(
    [
        html.Div([
                'How many days in the past do you want to see?', #Dropdown instructions 
                dcc.Dropdown(
                    id = 'Dropdown', 
                    options=[
                        {'label': '7 days', 'value': 7},
                        {'label': '14 days', 'value': 14},
                        {'label': '30 days', 'value': 30}
                    ],
                value=14,
                clearable=False
                )], style={'width': '30%', 
                    'display': 'inline-block', 
                    'marginBottom': 20, 
                    'marginTop': 20,
                    'marginLeft': 30}), #closes dropdown html.Div

        dcc.Graph(id='graph1') # this is the graph we add
    ]
)

@app.callback(
    Output(component_id='graph1', component_property='figure'),
    [Input(component_id = 'Dropdown', component_property = 'value')]
)
def update_output(input_value):
    random_x = data_clean.iloc[len(data_clean)-input_value:len(data_clean),0]
    random_y = data_clean['duration'].dt.seconds/60/60
    hover = data_clean['polarity']
    
    figure = {
        'data': [
            {'x':random_x, 'y':random_y, 'type':'bar', 'name': 'Series1', 'hovertext': hover}
        ],
        'layout': {
        }
    }
    return figure