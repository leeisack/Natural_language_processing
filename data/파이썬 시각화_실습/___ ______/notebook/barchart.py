from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.embed import components

# Simulated data.
a = ['B', 'D', 'C', 'A' ]
b = [40, 35, 55, 90]

# Define the output file.
# output_file("barchart.html")

# Create the bar chart.
f = figure(x_range = ['A', 'B', 'C', 'D' ])
f.vbar(x=a,top=b,bottom=0,width = 0.5)

# Interface.
my_js,my_div=components(f)

# Show the figure on the browser.
# show(f)