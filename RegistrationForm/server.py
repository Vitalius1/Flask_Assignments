from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    


app.run(debug=True)