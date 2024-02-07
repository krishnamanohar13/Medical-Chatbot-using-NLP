from flask import Flask, render_template, request, jsonify 
from chat import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_message = request.json['user_message']
    bot_response = get_response(user_message)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
