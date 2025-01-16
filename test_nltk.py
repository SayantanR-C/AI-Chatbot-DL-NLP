import nltk

# Download 'punkt' tokenizer if not already downloaded
nltk.download('punk_tab')

from nltk.tokenize import word_tokenize

# Example usage
sentence = "Hello! How are you doing today?"
tokens = word_tokenize(sentence)
print(tokens)
