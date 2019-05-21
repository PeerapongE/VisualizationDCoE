# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:20:59 2019

@author: PeerapongE
"""

import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
                      html.H1('Hello Dash'),
                      html.Div([
                                html.P('Dash converts Python classes into HTML'),
                                html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
                              ])
                      ])

# =============================================================================
# which gets converted (behind the scenes) into the following HTML in your web-app:
# <div>
#     <h1>Hello Dash</h1>
#     <div>
#         <p>Dash converts Python classes into HTML</p>
#         <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
#     </div>
# </div>
# =============================================================================

if __name__ == '__main__':
    app.run_server()
