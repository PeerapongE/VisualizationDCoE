#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output # Add more input output for dash call back

import plotly.graph_objs as go

import pandas as pd


# In[ ]:


# for plotly plot visualization (no need)
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)


# ### Prepare plotly figure

# In[ ]:


# 1- read data
watch_df = pd.read_excel('watch_data_aggregated_nopic.xlsx', sheet_name = 'ALL')
watch_df.head()


# ## Prepare the dropdown
# 
# Link to dataframe to get all avaialable option

# In[ ]:


size_unique = watch_df['Size'].dropna().unique()
size_unique


# In[ ]:


size_options = []

for size in size_unique:
    size_options.append({'label':size.capitalize(),'value':size})
    
size_options


# ### Prepare Dash
# 
# Now add dropdown
# 
# https://dash.plot.ly/dash-core-components/dropdown

# In[ ]:


app = dash.Dash() # create dash application


# In[ ]:


app.layout = html.Div([ html.H1('Price Distribution of Luxury watch'), # H1: header
                        html.H2('Select Watch Size'), # H2: header
                       
                        dcc.Dropdown(id = 'size-picker', #add Dropdown
                                     options = size_options,
                                     value = 'Please Select Size'), 
                    
                        dcc.Graph( # ใช้ dcc.Graph
                                 id='box_plot', # ใส่ id ไปด้วย เพราะจะมีหลายตัว และใช้ตอนเรียก function
                                 #figure = fig_box_watch # ค่อยไปเรียกจาก callback
                                 ),
                       
                      ])


# ### Callback
# 
# ทุกครั้งที่มีการ update ค่าจาก input จะมีการเรียก function ตัวนี้

# In[ ]:


@app.callback(Output('box_plot', 'figure'), # output to id = 'box_plot', element inside = figure
              [Input('size-picker', 'value')])

def update_figure(selected_size): # will refer to value
    
    # perform filtering
    filtered_df = watch_df[watch_df['Size'] == selected_size]
    
    # sort value by price
    filtered_mean_df = filtered_df.groupby(['Brand']).mean()[['Price_THB']].dropna().sort_values('Price_THB', ascending = False)
    # get index after sorted
    brand_unique = filtered_mean_df.index
    brand_unique
    
    # Create fig object again with filtered data
    # Data
    data = [go.Box(
                y    = filtered_df['Price_THB'][filtered_df['Brand'] == brand],
                name = brand
              )
        
            for brand in brand_unique
           ]
    
    # Layout
    layout = go.Layout(title = 'ราคา นาฬิกาหรู ตาม Brand แยกตาม Size',
                    yaxis=dict(
                               range = [0, 20000000],
                               autorange=False,
                               title = 'Price THB'
                              )
                      )
    
    # fig
    fig_box_watch = go.Figure(data   = data,
                              layout = layout)

    return fig_box_watch


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Run Dash server

# In[ ]:


if __name__ == '__main__':
    app.run_server()


# In[ ]:





# In[ ]:





# In[ ]:




