from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome! Go to /puppylatin/name to see your name in puppy latin!</h1>"

@app.route('/puppylatin/<name>')
def puppylatin(name):
    if name[-1] == "y":
         return f"<h1>Hi {name.capitalize()}!\nYour name in puppylatin is {name[:len(name)-1].capitalize()}" + "iful</h1>"
    else:
        return f"<h1>Hi {name.capitalize()}!\nYour name in puppylatin is {name.capitalize()}" + "y</h1>"


if __name__ == '__main__':
    app.run(debug=True)
