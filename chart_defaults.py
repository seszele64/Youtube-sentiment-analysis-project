# set plotly pio to dark theme
import plotly.io as pio

pio.templates.default = "plotly_dark"

# default font -> monospace
pio.templates[pio.templates.default].layout['font']["family"] = "monospace"

pio.templates[pio.templates.default].layout.margin.l = 50  # Left margin
pio.templates[pio.templates.default].layout.margin.r = 50  # Right margin
pio.templates[pio.templates.default].layout.margin.t = 50  # Top margin
pio.templates[pio.templates.default].layout.margin.b = 50  # Bottom margin

pio.templates[pio.templates.default].layout.hoverlabel.font.family = 'monospace'
pio.templates[pio.templates.default].layout.hoverlabel.font.size = 14
pio.templates[pio.templates.default].layout.hoverlabel.bgcolor = 'black'
pio.templates[pio.templates.default].layout.hoverlabel.bordercolor = 'lightgrey'

pio.templates[pio.templates.default].layout.images = [
    dict(
        source="https://upload.wikimedia.org/wikipedia/commons/3/33/Vanamo_Logo.png",  # URL to the logo image
        xref="paper",  # Use 'paper' for positioning relative to the whole canvas
        yref="paper",  # Use 'paper' for positioning relative to the whole canvas
        x=1,  # Logo position on the x-axis (1 is right on the canvas)
        y=1,  # Logo position on the y-axis (1 is top on the canvas)
        sizex=0.2,  # Specify the size of the logo on the x-axis (relative to the canvas width)
        sizey=0.2,  # Specify the size of the logo on the y-axis (relative to the canvas height)
        xanchor="right",  # Anchor point of the logo for x position
        yanchor="top",  # Anchor point of the logo for y position
        opacity=0.8  # Logo opacity
    )
]