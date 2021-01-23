
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/robot")
def robotindex():
    return render_template("index.html")


@app.route("/ask/<question>")
def talk(question=None):




    return "111"









if __name__ == '__main__':

    app.run(host='127.0.0.1', debug=True)
