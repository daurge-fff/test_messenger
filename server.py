from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/status')
def status():
    return f'Ok. Time: {time.asctime()}'

if __name__ == '__main__':
    app.run()