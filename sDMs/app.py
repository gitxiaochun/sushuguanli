from flask import Flask,render_template

app = Flask(__name__,)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/a1-1')
def a11():
    return render_template('1-1.html')
@app.route('/a1-2')
def a12():
    return render_template('1-2.html')
@app.route('/a2-1')
def a21():
    return render_template('2-1.html')
@app.route('/a2-2')
def a22():
    return render_template('2-2.html')
@app.route('/a2-3')
def a23():
    return render_template('2-3.html')
@app.route('/a3-1')
def a31():
    return render_template('3-1.html')
@app.route('/a3-2')
def a32():
    return render_template('3-2.html')
@app.route('/a3-3')
def a33():
    return render_template('3-3.html')
@app.route('/a3-4')
def a34():
    return render_template('3-4.html')
@app.route('/a4-1')
def a41():
    return render_template('4-1.html')
@app.route('/a4-2')
def a42():
    return render_template('4-2.html')
@app.route('/a4-3')
def a43():
    return render_template('4-3.html')
@app.route('/a4-4')
def a44():
    return render_template('4-4.html')
@app.route('/a4-5')
def a45():
    return render_template('4-5.html')
@app.route('/a5-1')
def a51():
    return render_template('5-1.html')
@app.route('/a5-2')
def a52():
    return render_template('5-2.html')
@app.route('/a6-1')
def a61():
    return render_template('6-1.html')
@app.route('/a6-2')
def a62():
    return render_template('6-2.html')
@app.route('/a6-3')
def a63():
    return render_template('6-3.html')
@app.route('/a6-4')
def a64():
    return render_template('6-4.html')

@app.route('/a7-1')
def a71():
    return render_template('7-1.html')
@app.route('/a8-1')
def a81():
    return render_template('8-1.html')
@app.route('/a8-2')
def a82():
    return render_template('8-2.html')
if __name__ == '__main__': 
    app.run(host='0.0.0.0') 