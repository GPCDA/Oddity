################################################################################
#                                  scatterplots.py
#               Author: Fernando Rosendo (franplt629@gmail.com)
################################################################################

#Remember all dataframe columns are converted to uppercase
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
# for use on the callback
from app import app, df

#colors 
color = {
    'background':'#FFFFFF',
    'text':'#000000'
}

#font
font = {
    'size':15,
    'family':'helvetica'
}

#Helper func for the extra data callback

def helper_func(ser):
    out = [html.P(str(ind)+' => '+str(val)) for ind, val in zip(ser.index,
                                                                ser.values)]
    if df.index.name is None:
        out.insert(0, html.P('INDICE => ' + str(ser.name)))
    else:
        out.insert(0, html.P(str(df.index.name).upper()+' => '+str(ser.name)))

    return html.Div(out)


layout = html.Div([

#Dropdown with label
    html.Div([
        html.Label('X'),
        dcc.Dropdown(
            id='x-value',
            options = [{'label': i, 'value':i} for i in df.columns],
            value=[]
        ),

        html.Label('Y'),
        dcc.Dropdown(
            id='y-value',
            options = [{'label': i, 'value':i} for i in df.columns],
            value=[]
        )
    ],className='container'),

#Button for plotting(cause of huge ds)
    html.Div([
        html.Button(id='button-sp',n_clicks=0,
                   children='Plotar', className='btn btn-primary')
    ],className='container',style={'marginTop':10}),

#Graph itself
    dcc.Graph(id='output-scatterplot'),

#Extra data
    html.Div(id='data-scatterplot')
])

#Callback for the graph itself(scatterplot)
@app.callback(Output('output-scatterplot','figure'),
             [Input('button-sp','n_clicks')],
             [State('x-value','value'),
             State('y-value','value')])
def update_graph(n_clicks,x,y):
#data object go.Scattergl(lighter than Scatter)
    data = [go.Scattergl(
        x = df[ (df['CLUSTER']==cluster) & (df['ANOMALY'] == 1) ][x],
        y = df[ (df['CLUSTER']==cluster) & (df['ANOMALY'] == 1) ][y],
        mode = 'markers',
        name = 'Cluster ' + str(cluster) + ' sem poss. anom.',
        marker = dict(
            size=10,
            line=dict(
                width=1.5
            )
        )
    ) for cluster in df['CLUSTER'].unique()]

    data_anomaly = [go.Scattergl(
        x = df[df['ANOMALY'] == -1][x],
        y = df[df['ANOMALY'] == -1][y],
        mode = 'markers',
        name = 'Poss. Anomalia',
        text = list(map(lambda x: 'Cluster ' + x, map(str, df[df['ANOMALY'] ==
                                                             -1]['CLUSTER'].values))),
        marker = dict(
            size = 12.5,
            color = 'rgb(255,0,0)',
            line = dict(
                width=1.5
            )
        )
    )]

    data.extend(data_anomaly)

#go.Layout object
    layout = go.Layout(
        hovermode='closest',
        plot_bgcolor=color['background'],
        paper_bgcolor=color['background'],
        font=dict(
            color=color['text']
        )
    )

#go.Figure object
    fig = go.Figure(data=data, layout=layout)

    return fig

#Callback for the data-scatterplot
@app.callback(Output('data-scatterplot','children'),
             [Input('output-scatterplot', 'clickData'),
             Input('x-value', 'value'),
             Input('y-value','value')])
def callback_edata(clickData, x ,y):
    x_sel = clickData['points'][0]['x']
    y_sel = clickData['points'][0]['y']

#Related series to the selection
    rel_ser = df[(df[x]==x_sel) & (df[y]==y_sel)].iloc[0]

    return html.Div([
        html.H1('Dados do Ponto Selecionado', className='display-4'),
        html.P(f'Você selecionou o ponto nas coordenadas ( x = {x_sel} , y = {y_sel} )',
               className='lead'),
        html.Hr(className='my-4'),
        helper_func(rel_ser)
    ], className='jumbotron')
