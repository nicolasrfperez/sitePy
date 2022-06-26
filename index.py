from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')

def about():
    return render_template('about.html')

<<<<<<< HEAD
@app.route('/personal')

def personal():
    return render_template('personal.html')

=======
@app.route('/principal')

def principal():
    return render_template('principal.html')
    
>>>>>>> 8dafac9 (probando ubuntu)
if __name__ == '__main__':
    app.run(debug=True)