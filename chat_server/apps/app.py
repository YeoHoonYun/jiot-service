from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('index.html', name="Alex")

if __name__ == '__main__':
    app.run(debug=True)
    # http://127.0.0.1:5000/hello