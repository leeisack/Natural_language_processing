from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import Range1d, ColumnDataSource
from bokeh.models.annotations import LabelSet
from bokeh.models.widgets import Select
from bokeh.layouts import layout

# Define the data.
my_data = ColumnDataSource({'x':[1,2,3,4,5], 'y': [2,5,3,4,1], 'name1': ['1', '2', '3', '4', '5'],'name2': ['A', 'B', 'C', 'D', 'E']}) 

# Define the figure.
f=figure()
f = figure()
f.plot_width=700                                
f.plot_height=500                               
f.background_fill_color="yellow"                
f.background_fill_alpha=0.1
f.circle(x='x', y='y', fill_alpha = 0.5, color='green', size=10, source=my_data)

# Define the LabelSet.
my_labelset = LabelSet(x='x', y='y', text='name1', x_offset = 5, y_offset=5, source=my_data)
f.add_layout(my_labelset)

# Instantiate the Widget.
my_select = Select(title="SELECT THE LABEL SET:", options=[("name1","Label Set #1"),("name2","Label Set #2")])

# Event-handling function.
def callback(x,old,new):
    my_labelset.text = my_select.value

# Bind the event with the event-handling function.
my_select.on_change("value", callback)

# Display.
my_layout = layout([[my_select]])
curdoc().add_root(f)
curdoc().add_root(my_layout)



