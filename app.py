from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/studybot', methods=['POST'])
def studybot():
    user_input = request.json.get("question")
    response = f"You asked: {user_input}. Here’s a study tip: Stay curious!"
    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
