from flask import *
from gpiozero import LED
from time import sleep
from traffic_controls import * 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
