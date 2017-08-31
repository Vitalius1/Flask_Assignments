from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def get_color():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    print red, green, blue
    return render_template('index.html', red=red, green=green, blue=blue)

app.run(debug=True)