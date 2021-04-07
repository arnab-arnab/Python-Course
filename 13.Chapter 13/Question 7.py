from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Devesh Doggy Hai"

app.run(debug=True)
