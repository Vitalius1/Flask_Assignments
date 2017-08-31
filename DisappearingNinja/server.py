from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
   return render_template('ninjas.html')

@app.route('/ninja/<arg>')
def ninja(arg):
    choice = {'blue' : 'leonardo.jpg', 'orange' : 'michelangelo.jpg', 'red' : 'raphael.jpg', 'purple' : 'donatello.jpg'}
    for key in choice:
        if key == arg:
            return render_template("ninja.html", src = choice[key])
    for key in choice:
        if arg != key:
            return render_template("ninja.html", src = "notapril.jpg")

app.run(debug = True)