from flask import Flask, render_template
import
app = Flask(__name__)
@app.route('/')
def index():
    context =
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)