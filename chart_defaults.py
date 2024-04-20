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
