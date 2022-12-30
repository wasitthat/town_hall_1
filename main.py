from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/02_box_model.html')
def sample():
    return render_template('02_box_model.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')


@app.route('/toobin')
def toobin():
    return render_template('toobin.html')


@app.route('/sampson')
def sampson():
    return render_template('sampson.html')


@app.route('/chua')
def chua():
    return render_template('chua.html')


@app.route('/sorkin')
def sorkin():
    return render_template('sorkin.html')

@app.route('/luncheons')
def luncheons():
    return render_template('luncheons.html')
if __name__ == "__main__":
    app.run(debug=True)
