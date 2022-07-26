from flask import Flask, redirect, render_template, request, url_for
from face import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/myimage')
def myImage():
    return render_template("myimage.html")

@app.route('/resultimage')
def resultImage():
    return render_template("resultimage.html")
    
@app.route('/naver')
def naver():
    return 'I\'m Naver'

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        imageLink = request.form['imageLink']
        main(imageLink)
        return redirect(url_for('resultImage'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)