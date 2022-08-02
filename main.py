import pandas as pd
import plotly.express as px
import dash
from dash import Dash,dcc,html,Input,Output

#Lectura de datos
url= 'https://raw.githubusercontent.com/Janiopi/ProyectoFormativo/main/Archivo.csv'
df = pd.read_csv(url)

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
#Titulo y subtitulo
        html.H1('Variación del índice del PBI'),
        html.H2('Año de referencia: 2007'),

#Menu desplegable
    dcc.Dropdown(id='my_dropdown',
        options=[
                {'label': 'Índice global', 'value': 'Índice Global'},
                {'label': 'Agricultura,ganadería,caza y silvicultura', 'value': 'Agricultura, ganadería, caza y silvicultura '},
                {'label': 'Pesca y acuicultura', 'value': 'Pesca y acuicultura '},
                {'label': 'Extraccion de petróleo,gas y minerales', 'value': 'Extraccion de petróleo, gas, minerales y servicios conexos '},
                {'label': 'Manufactura', 'value': 'Manufactura '},
                {'label': 'Electricidad,gas,agua y saneamiento', 'value': 'Electricidad, gas, suministro de agua, alcantarillado y gestión de desechos y saneamiento '},
                {'label': 'Construcción', 'value': 'Construcción '},
                {'label': 'Comercio y mantenimiento de vehículos', 'value': 'Comercio y mantenimiento y reparación de vehículos automotores y motocicletas '},
                {'label': 'Otros servicios', 'value': 'Otros Servicios'},
                {'label': 'Importación y otros impuestos', 'value': 'Derechos de Importación y Otros Impuestos a los productos (*)'},
            ],
            optionHeight=35,
            value='Índice Global', #Valor por defecto
            searchable=True, #Nos permite digitar
            placeholder='Elija una opción: ', #Temporal
            clearable=True,
        ),

    dcc.Graph(id='graph_output', figure={}),


        ]


    )

#LLamada
@app.callback(
    Output(component_id='graph_output',component_property='figure'),
    [Input(component_id='my_dropdown',component_property='value')],
    prevent_initial_call=False
)
#Actualizar grafico
def update_graph(val_chosen):
    if len(val_chosen)>0:
        print(f"El valor escogido es: {val_chosen} ")
        print(type(val_chosen))
        fig=px.line(df,x='Año y Mes',y=val_chosen)
        return fig
    elif len(val_chosen)== 0:
        raise dash.exceptions.PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True)