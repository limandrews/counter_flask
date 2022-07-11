from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "anystring"

@app.route('/')
def index():
    if 'stringcount' in session:
        print('key exists!')
        session['stringcount'] += 1
    else:
        session['stringcount'] = 0
        print("key 'stringcount' does NOT exist")
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)