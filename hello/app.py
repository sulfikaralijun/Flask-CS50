from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/greet')
# def index():
#     name = request.args.get('name', 'World')
#     return render_template('index.html', name=name)
@app.route('/')
def indexs():
    return render_template('index.html')