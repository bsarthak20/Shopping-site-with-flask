# flask is a library of python it is recalled in small letters, the Flask is a class of module flask 

from flask import Flask, render_template

app = Flask(__name__)   # app is an object or instance of a class Flask

@app.route("/")
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)