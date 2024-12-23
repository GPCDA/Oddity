################################################################################
#                                  boxplots.py
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
        html.Label('Y'),
        dcc.Dropdown(
            id='y-value',
            options = [{'label': i, 'value':i} for i in df.columns],
            value=[]
        )
    ],className='container'),

#Button for plotting(Cause of huge ds)
    html.Div([
        html.Button(id='button-bp',n_clicks=0,
                   children='Plotar', className='btn btn-primary')
    ],className='container', style={'marginTop':10}),

#Graph itself
    dcc.Graph(id='output-boxplot'),

#Extra data
    html.Div(id='data-boxplot')
])

#Callback for the graph itself(boxplot)
@app.callback(Output('output-boxplot','figure'),
             [Input('button-bp','n_clicks')],
             [State('y-value','value')])
def update_graph(n_clicks,y):
    #Creating data object go.Box
    data = [go.Box(
        y = df[df['CLUSTER'] == cluster][y],
        name = 'Cluster ' + str(cluster)
    ) for cluster in df['CLUSTER'].unique()]

#Creating go.Layout object
    layout = go.Layout(
        hovermode='closest',
        plot_bgcolor=color['background'],
        paper_bgcolor=color['background'],
        font = dict(
            color=color['text']
        )
    )
#Creating go.Figure object
    fig = go.Figure(data=data, layout=layout)
    return fig

#Callback for the data-boxplot
@app.callback(Output('data-boxplot','children'),
             [Input('output-boxplot', 'clickData'),
             Input('y-value','value')])
def callback_edata(clickData, y):
    if len(clickData['points']) != 1:
        return html.Div([
            html.H2('Por favor selecione um só ponto e tente novamente.'),
            html.P('Se você selecionar um só ponto, posso dar informações a respeito desse ponto.'),
            html.Hr(),
            html.P('Sei que estamos num boxplot, selecione um dos outliers mostrados no gráfico clicando em cima do ponto.')
        ], className='alert alert-warning')

    x_sel = clickData['points'][0]['x']
    y_sel = clickData['points'][0]['y']

#Related series to the selection
    rel_ser = df[df[y]==y_sel].iloc[0]

    return html.Div([
        html.H1('Dados do Ponto Selecionado', className='display-4'),
        html.P(f'Você selecionou o ponto na coordenada ( x = {x_sel} , y = {y_sel} )',
               className='lead'),
        html.Hr(className='my-4'),
        helper_func(rel_ser)
    ], className='jumbotron')
