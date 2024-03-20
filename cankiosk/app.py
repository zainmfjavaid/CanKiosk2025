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

# Guest experience routes
@app.route('/guest')
def guest_root():
    return render_template('guest.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)