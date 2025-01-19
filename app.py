from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Storage for messages (in-memory)
messages = []

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Get all messages."""
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def post_message():
    """Add a new message."""
    data = request.json
    if 'name' in data and 'message' in data:
        new_message = {
            "name": data['name'],
            "message": data['message']
        }
        messages.append(new_message)
        return jsonify({"status": "success", "message": "Message added!"}), 201
    return jsonify({"status": "error", "message": "Invalid data."}), 400

if __name__ == '__main__':
    app.run(debug=True)
