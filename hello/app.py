from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def indexs():
    return render_template('index.html')

@app.route('/greet' , methods=['POST'])
def greet():
    name = request.form.get('name', 'Anonym')
    return render_template('greet.html', name=name)