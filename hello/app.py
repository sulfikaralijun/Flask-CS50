from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def indexs():
    if request.method == 'POST':
        name = request.form.get('name', 'Anonym')
    return render_template('index.html')