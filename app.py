import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'DC Metro'
myheading1 = 'Not a fan!'
myheading2 = 'Hurry! The orange train is coming.'
image1 = 'favicon.ico'
image2 = 'arr.jpeg'
textbody = "Metro's recent on time performance ratings are so good, it's getting harder to find a good reason to take a car!"
sourceurl = 'https://www.wmata.com/about/back2good/index.cfm'
githublink = 'https://github.com/austinlasseter/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '12px',
                'font-size': '28px',
                'height': '150px',
                'border': 'thin red solid',
                'color': 'rgb(213, 54, 0)',
                'backgroundColor': 'rgb(180, 219, 242)',
                'textAlign': 'center',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
