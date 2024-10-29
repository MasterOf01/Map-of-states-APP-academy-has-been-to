import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig=go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['number students'].astype(float),
    locationmode='USA-states',
    colorscale='Teal',
    colorbar_title='most to least visited'
))

fig.update_layout(
    title_text="APP ACADEMY USA VISITS",
    geo_scope="usa"
)

fig.show()