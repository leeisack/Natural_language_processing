from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import Range1d, ColumnDataSource
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout

# Instantiate the Widgets.
my_input = TextInput(value="")
my_button = Button(label = "Click Me!")
my_output = Paragraph()

# Event-handling function.
def callback():
    my_output.text = my_input.value

# Bind the event with the event-handling function.
my_button.on_click(callback)

# Display.
my_layout = layout([[my_output],[my_input,my_button]])
curdoc().add_root(my_layout)

