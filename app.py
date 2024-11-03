from flask import Flask, render_template
import datetime as date
app = Flask(__name__)

@app.route('/')
def index():
    age = date.datetime.now().year-2010 if date.datetime.now().month >= 10 else date.datetime.now().year-2010-1
    return render_template('index.html', age=age)

if __name__ == '__main__':
    app.run(debug=True)