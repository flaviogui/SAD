import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv(r'C:\Users\SAMSUNG\Desktop\7º P\SAD\Dashboard\sales_data_sample.csv', encoding='latin1')


# Conversão da coluna de data (ajuste conforme o nome da sua coluna)
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')

# Inicializar o app
app = dash.Dash(__name__)
app.title = "Sales Dashboard"

# Layout do app
app.layout = html.Div([
    html.H1("Sales Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Selecione o Produto:"),
        dcc.Dropdown(
            options=[{'label': i, 'value': i} for i in df['ProductLine'].unique()],
            value=df['ProductLine'].unique()[0],
            id='product-dropdown'
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='sales-over-time'),

    dcc.Graph(id='sales-by-country')
])

# Callbacks
@app.callback(
    [Output('sales-over-time', 'figure'),
     Output('sales-by-country', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_graphs(selected_product):
    dff = df[df['ProductLine'] == selected_product]

    # Gráfico de vendas ao longo do tempo
    fig_time = px.line(
        dff.groupby('OrderDate')['Sales'].sum().reset_index(),
        x='OrderDate',
        y='Sales',
        title=f'Vendas ao longo do tempo - {selected_product}'
    )

    # Gráfico de vendas por país
    fig_country = px.bar(
        dff.groupby('Country')['Sales'].sum().reset_index(),
        x='Country',
        y='Sales',
        title=f'Vendas por País - {selected_product}'
    )

    return fig_time, fig_country


# Rodar o app
if __name__ == '__main__':
    app.run_server(debug=True)
