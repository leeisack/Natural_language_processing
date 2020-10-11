# Bokeh Embedding with Flask.
from flask import Flask, render_template
from barchart import my_js, my_div     # Extract the JS and div from the Bokeh figure as if it were a module!

# Instantiate the app.
app = Flask(__name__)

# Index page function.
@app.route("/")
def index():
    return render_template("index.html", js=my_js, div=my_div)

# Run.
if __name__ == "__main__":
    app.run(debug=True)