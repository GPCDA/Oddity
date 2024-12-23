################################################################################
#                                  index.py
#               Author: Fernando Rosendo (franplt629@gmail.com)
################################################################################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import boxplots, scatterplots, home

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
#Navbar
    html.Nav([
#Brand navbar
        html.A('Oddity', href='/',
              className='navbar-brand'),
#Div dentro da navbar
        html.Div([
#Ul dentro da div
            html.Ul([
#Serie de listitems dentro da Ul
                html.Li([
                    html.A('Home',href='/',
                            className='nav-link')
                ], className='nav-item active'),
                html.Li([
#Changed dcc.Link to html.A just to make it refresh
                    html.A('Boxplots',href='/box',
                            className='nav-link')
                ], className='nav-item active'),
                html.Li([
                    html.A('Scatterplots',href='/scatter',
                            className='nav-link')
                ], className='nav-item active')

            ], className='navbar-nav')
        ] ,id='navbarNav')
    ], className='navbar navbar-expand-lg navbar-light bg-light'),
#Navbar pronta aqui em cima
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url','pathname')])
def update_content(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/box':
        return boxplots.layout
    elif pathname == '/scatter':
        return scatterplots.layout
    else:
        return html.H1('404')
    # Can add a 404.py page later on

if __name__ == "__main__":
    app.run_server()
