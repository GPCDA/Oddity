import dash
import pandas as pd

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

display_df = pd.read_csv('display_example.csv', index_col=0)
df = pd.read_csv('base.csv', sep=';')
df.columns = [item.upper() for item in df.columns]
