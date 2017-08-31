from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.counter = 0

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html')

@app.route('/plustwo')
def increment():
    session['counter'] += 1  # we add 1 cause redirecting to the root route increments it by 1 too.
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0  # same thing as incrementing by two
    return redirect('/')

app.run(debug=True) 