from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route("/info")
def info():
    return "<h1>Puppys are cute!</h1>"

@app.route('/puppy/<name>') #this is for dynamic routing
def puppy(name):
    return f"100th letter: {name[100]}"
    # return f"<h1>This is a page for {name.upper()}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
