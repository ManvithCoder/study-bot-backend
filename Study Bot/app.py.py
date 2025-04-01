from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/studybot', methods=['POST'])
def studybot():
    user_input = request.json.get("question")
    response = f"You asked: {user_input}. Here’s a study tip: Stay curious!"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
