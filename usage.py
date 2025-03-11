import dash_dangerously_set_inner_html
from dash import Dash, html

app = Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
        <h1>Header</h1>
    '''),
])

if __name__ == '__main__':
    app.run(debug=True)
