# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:48:27 2023

@author: Rashmi_PC
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:09:23 2023

@author: Rashmi_PC
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
data=pd.read_csv('C:\\Users\\Rashmi_PC\\Downloads\\SampleSuper.csv')
d1=pd.pivot_table(data=data,index='Category',columns='Region',values='Sales',aggfunc=np.sum)
#d=pd.pivot_table(data=data,index='Category',columns='Region',values='Sales',aggfunc=np.sum).plot(figsize=(5,5),title="Sales for category in different regions",kind='bar')
# look for the link "http://127.0.0.1:8050/" to get the dash board.
d2=pd.pivot_table(data=data,index='Category',columns='Region',values='Profit',aggfunc=np.sum)

d3=pd.pivot_table(data=data,index='Category',values='Profit',aggfunc=np.sum)
d4=pd.pivot_table(data=data,index='Region',values='Profit',aggfunc=np.sum)
d5=pd.pivot_table(data=data,index='Region',values='Sales',aggfunc=np.sum)

from dash import Dash, html, dcc, dash_table
#import dash_html_components as html
#import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)



markdown_txt=''' My Dash Board for SuperStore Data set
'''

markdown_text2=''' * Shows Total sales vs Category plot for different regions. it can be seen that sales in southern region are least for all categories.
* All regions are showing almost same sale for different cateories.
* Sales team for southern and central region need to take necessary steps'''

markdown_text3='''  * Shown Total profit in different categories for different regions. 
* Furniture category is providing least profit in all regions. Furniture category is showing loss in central region.
 * Office supplies and technology categories are giving good profit in East and West regions.
* Profits from southern region need to monitored.
'''

markdown_text4=''' * It can be seen from fig 3, fig 4 and fig 5 plots that technology category is generating maximum profit while furniture 
category is giving minimum profit. 
* Region wise profit is: highest for western region, next max. is eastern region , then southern region and central region is giving minimum  profit.
* Even though the sales of central region is more as compare to southern region, the profit by southern region is more as compare
to central region.'''
fig1 = px.bar(d1,barmode="group",title=' Fig.1 Total sales of different category items in different regions',labels={'x':'Category','y':'Total Sales'})
fig1.update_layout(yaxis_title="total sale")

fig2 = px.bar(d2,barmode="group",title='Fig.2 Total profit of different category items in different regions')
fig2.update_layout(yaxis_title="total Profit")

fig3=px.bar(d3,barmode="group",title='Fig.3 Category with total profit')
fig3.update_layout(yaxis_title="total Profit")

fig4=px.bar(d4,barmode="group",title='Fig.4 Region with total Profit')
fig4.update_layout(yaxis_title="total Profit")

fig5=px.bar(d5,barmode='group',title='Fig.5 Total sales for each region')
fig5.update_layout(yaxis_title="total sale")


app.layout = html.Div([html.Div(children=[
    html.H1(children='SuperStore',style={'textAlign':'center'})]),

html.Div([dcc.Markdown(children=markdown_txt,style={'textAlign':'center'})]),

html.Div([dbc.Row([
    dbc.Col(dcc.Graph(
        id='example-graph',
        figure=fig1),width=4,style={'display':'inline-block','vertical-align':'top'})
        ###,responsive=False,style={'height':1000,'width':1000,'display':'inline','allign':'center'}
    , 
    
    
    #html.Div([html.H4(children='US Agriculture Exports (2011)'),
    #generate_table(d1)]),
dbc.Col(dcc.Graph(
        id='example-graph1',
        figure=fig2),width=4,style={'display':'inline-block','vertical-align':'top'}), 


],justify='center', align='start')
    ]),


html.Div([dbc.Row([dbc.Col(dcc.Markdown(children=markdown_text2),width=4,style={'display':'inline-block','vertical-align':'top'}),
    
 


dbc.Col(dcc.Markdown(children=markdown_text3),width=4,
        style={'display':'inline-block','vertical-align':'top'})],justify='center', align='start')])

,

html.Div([dbc.Row([dbc.Col(dcc.Graph(id='example-graph3',figure=fig3),width=3,style={'display':'inline-block','vertical-align':'top'}),

#html.Div([dcc.Markdown(children=markdown_text4)]),

dbc.Col(dcc.Graph(id='example4',figure=fig4),width=3,style={'display':'inline-block','vertical-align':'top'}),
dbc.Col(dcc.Graph(id='example5',figure=fig5),width=3,style={'display':'inline-block','verticle-align':'top'})],
                  justify='center',align='start')]),


html.Div([dcc.Markdown(children=markdown_text4)])

])


'''',style={'height':100,'width':100,'display':'inline','allign':'left'})])'''

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
#if name=='main':
    app.run_server(debug=True)