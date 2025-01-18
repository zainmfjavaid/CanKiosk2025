from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def idle():
    return render_template('idle.html')


@app.route('/index')
def home():
    return render_template('index.html')

# Judge experience routes
@app.route('/judge')
def judge_root():
    return render_template('judge.html')

@app.route('/judge/description')
def judge_description():
    return render_template('judge/description.html')

@app.route('/judge/robot')
def judge_robot():
    return render_template('judge/robot.html')

@app.route('/judge/cad')
def judge_cad():
    return render_template('judge/cad.html')

@app.route('/judge/manufacturing')
def judge_manufacturing():
    return render_template('judge/manufacturing.html')

@app.route('/judge/programming')
def judge_programming():
    return render_template('judge/programming.html')

@app.route('/judge/business')
def judge_business():
    return render_template('judge/business.html')

@app.route('/judge/community')
def judge_community():
    return render_template('judge/community.html')

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
    app.run(host='0.0.0.0', port=3000, debug=True)