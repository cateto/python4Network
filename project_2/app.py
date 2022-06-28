from flask import Flask, render_template, request
from ckonlpy.tag import Twitter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.get('data')
    twitter = Twitter()
    result = twitter.morphs(data)
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)