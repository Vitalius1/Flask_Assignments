from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'my_secret'

@app.route('/')
def index():
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def win():
    time = datetime.now()
    print time ## debug
    session['total']
    loose = None
    if request.form['building'] == 'farm':
        coins = random.randrange(10, 21)
        session['total'] += coins
        print "======" + str(session['total'])
        session['activity'].insert(0, (coins, "farm", time, loose))
        print session['activity']  ## debug
    elif request.form['building'] == 'cave':
        coins = random.randrange(5, 11)
        session['total'] += coins
        session['activity'].insert(0, (coins, "cave", time, loose))
    elif request.form['building'] == 'house':
        coins = random.randrange(2, 6)
        session['total'] += coins
        session['activity'].insert(0, (coins, "house", time, loose))
    elif request.form['building'] == 'casino':
        chance = random.randrange(0,2)
        print chance  ## debug
        if chance == 1:
            coins = random.randrange(0,51)
            session['total'] += coins
            session['activity'].insert(0, (coins, "casino", time, loose))
        else:
            loose = 0
            coins = random.randrange(0,51)
            session['total'] -= coins
            session['activity'].insert(0, (coins, "casino", time, loose))
    print session['total']  ## debug
    return redirect('/')

@app.route('/reset')
def reset():
    session['total'] = 0
    session['activity'] = []
    return redirect('/')

app.run(debug=True)