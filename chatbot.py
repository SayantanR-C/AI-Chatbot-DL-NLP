import random
import json
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Load the intents from the intents.json file
def load_intents():
    with open('intents.json') as file:
        intents = json.load(file)
    return intents['intents']

# Function to preprocess the user input
def preprocess_input(user_input):
    # Process the input through spaCy
    doc = nlp(user_input.lower())  # Convert input to lowercase and process it
    tokens = [token.lemma_ for token in doc if not token.is_stop]  # Lemmatize and remove stop words
    return tokens

# Function to get a response based on user input
def get_response(user_input):
    print(f"Received input: {user_input}")  # Debug log
    
    # Load intents from the JSON file
    intents = load_intents()

    # Preprocess the user input (tokenize and lemmatize)
    tokens = preprocess_input(user_input)
    print(f"Processed tokens: {tokens}")  # Debug log

    # Loop through the intents and check for matching patterns
    for intent in intents:
        for pattern in intent['patterns']:
            pattern_tokens = preprocess_input(pattern)
            # Check if any token from the input matches a token in the pattern
            if any(token in pattern_tokens for token in tokens):
                # Return a random response from the matched intent
                return random.choice(intent['responses'])
    
    # Default response if no match is found
    return "Sorry, I don't understand."
