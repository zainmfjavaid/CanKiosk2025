from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Judge experience routes
@app.route('/judge')
def judge_root():
    return render_template('judge.html')

# Scout experience routes
@app.route('/scout')
def scout_root():
    return render_template('scout.html')

@app.route('/scout/specs')
def scout_specs():
    return render_template('scout/specs.html')

@app.route('/scout/strategy')
def scout_strategy():
    return render_template('scout/strategy.html')

@app.route('/scout/auton')
def scout_auton():
    return render_template('scout/auton.html')

@app.route('/scout/documentation')
def scout_documentation():
    return render_template('scout/documentation.html')

# Guest experience routes
@app.route('/guest')
def guest_root():
    return render_template('guest.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)