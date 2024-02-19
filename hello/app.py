from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def indexs():
    return render_template('index.html')

@app.route('/greet' , methods=['GET'])
def greet():
    name = request.args.get('name', 'Anonym')
    return render_template('greet.html', name=name)