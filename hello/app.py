from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if "name" in 
    return render_template('index.html', placeholder=name)