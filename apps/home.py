################################################################################
#                                   home.py
#               Author: Fernando Rosendo (franplt629@gmail.com)
################################################################################
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
import pandas as pd
from app import display_df

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

layout = html.Div([
    html.H1('Instruções', style={'textAlign':'center'}),
    html.H3('Exemplo de base de dados válida'),
    html.Div(
            dt.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in display_df.columns],
            data=display_df.to_dict("rows")
            ), className='container', style={'marginLeft':10,
                                             'marginRight':10}),
    html.H3('Como preparar uma base de dados válida'),
    dcc.Markdown('''
Oddity pode trabalhar com qualquer base de dados. Os únicos requerimentos são
                 que a base deve estar descrita em formato **CSV** e
                 que suas anomalias e clusters estejam **rotulados conforme as
                 seguintes regras**:

* Anomalias devem estar numa coluna isolada, chamada
                 **Anomaly**, conforme a tabela descrita no início da página.
* A coluna Anomaly deve classificar os eventos com o rótulo
                 _**-1**_ para _outliers_ e _**1**_ para _inliers_.
* **Clusters** devem estar numa coluna isolada, chamada
                 **Cluster**, conforme a tabela descrita no início da página.
                 Não é necessário se preocupar com o tipo de dado que a coluna
                 possui nem com a quantidade de clusters rotulados.

***OBS:*** *Não é necessário se preocupar se os rótulos ou colunas
                 estão em caixa alta ou baixa (inclusive as colunas **Anomaly** e **Cluster**).
                 **Oddity** automaticamente converte as colunas da base de dados para
                 caixa alta.*

Quanto à base de dados utilizada, deve estar localizada na mesma pasta que o
                 arquivo principal do programa (***app.py***) e deve se chamar
                 '***base.csv***'
    ''')
], className='container', style={
    'marginLeft':20
})
