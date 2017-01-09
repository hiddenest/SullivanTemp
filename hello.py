#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/get")
def getter() :
    return render_template("name.html", name=request.args.get("name"))

@app.route("/post", methods=["POST"])
def poster() :
    return render_template("name2.html", name=request.form.get("name"))

@app.route("/")
def value():
    return render_template("index.html")

@app.errorhandler(404)
def forzerofor(e) :
    return "<img src='https://media.giphy.com/media/gpXfKa9xLAR56/giphy.gif'><h1 style='color:red'>그 친구 없다 전해라</h1>", 404

if __name__ == "__main__":
    app.run()
