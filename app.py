import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='./build/static')



@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

# Define a dictionary of Tarot cards and their interpretations
tarot_deck = {
    "Card1": "Interpretation 1 for Card 1",
    "Card2": "Interpretation 2 for Card 2",
    "Card3": "Interpretation 3 for Card 3",
    # Add more cards and interpretations as needed
}

# Define a route for Tarot readings
@app.route('/api/tarot-reading', methods=['GET'])
def generate_tarot_reading():
    # Number of cards to include in the reading (you can adjust this)
    num_cards = 3
    
    # Shuffle the Tarot deck
    shuffled_deck = list(tarot_deck.keys())
    random.shuffle(shuffled_deck)
    
    # Select a random set of cards for the reading
    selected_cards = shuffled_deck[:num_cards]
    
    # Retrieve interpretations for the selected cards
    interpretations = [tarot_deck[card] for card in selected_cards]
    
    # Return the Tarot reading as JSON data
    tarot_reading = {
        "cards": selected_cards,
        "interpretations": interpretations,
    }
    return jsonify(tarot_reading)

if __name__ == '__main__':
    app.run(debug=True)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)
