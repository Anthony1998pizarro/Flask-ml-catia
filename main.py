from flask import Flask,render_template,request
from controllers.process_controller import predict_text
import json

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/predic',methods=[ 'POST'])
def predic():
  if request.method == 'POST':
    text = request.get_json("answer")
    text = text['answer']
  return predict_text(text)

if __name__ == '__main__':
  app.run(debug=True)   