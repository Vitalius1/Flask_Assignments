from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'my_secret'

@app.route('/')
def index():
    if 'randnum' not in session:
        session['randnum'] = random.randrange(0, 101)
    print "Randnum is:", session['randnum']
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def compare():
    number = request.form['number']
    print "Your number is:", number, "Randnum is: ", session['randnum']
    if int(number) > session['randnum']:
        return render_template('index.html', result = "Too High!")
    elif int(number) < session['randnum']:
        return render_template('index.html', result = "Too Low!")
    elif int(number) == session['randnum']:
        return render_template('succes.html', result = number + " Nice you guessed it!")

@app.route('/again')
def reset():
    session.pop('randnum')
    return redirect('/')


app.run(debug=True)