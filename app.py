from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/hello')

def hello():
    return "Insight web app created by yourname."

if __name__ == '__main__':
    app.run(debug=True)
