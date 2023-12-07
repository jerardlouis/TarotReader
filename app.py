import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

# Define a route for Tarot readings
@app.route('/api/tarot-reading', methods=['GET'])
def generate_tarot_reading():
    # Your Tarot card reading logic goes here
    # Generate a random Tarot reading, select cards, and provide interpretations
    # Return the Tarot reading as JSON data
    tarot_reading = {
        "cards": ["Card 1", "Card 2", "Card 3"],  # Example Tarot cards
        "interpretations": ["Interpretation 1", "Interpretation 2", "Interpretation 3"],  # Example interpretations
    }
    return jsonify(tarot_reading)

if __name__ == '__main__':
    app.run(debug=True)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)
