from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "safe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def save_info():
    print "GOT the INFO and SAVED IT"
    
    # Start validation
    if len(request.form['name']) < 1:
        flash("This field can not be empty!", 'nameError')
        return redirect('/')
    if len(request.form['comments']) < 1:
        flash("This field can not be empty!", 'comError')
        return redirect('/')
    if len(request.form['comments']) > 120:
        flash("This comment is to long!", 'comError')
    # End validation

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comments']
    print name, location, language, comment # debug
    return render_template('results.html', name = name, loc = location, lang = language, comm = comment)

@app.route('/back')
def go_back():
    return render_template('index.html')

app.run(debug = True)