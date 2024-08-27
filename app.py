from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
        return "Hello, this is a Flask app running on port 5000 with debug mode!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

