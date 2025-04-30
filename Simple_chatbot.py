import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample conversation pairs (can be expanded)
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm just a bot, but I'm doing fine!", "I'm good. How can I help you?"]],
    [r"what is your name", ["I'm a simple chatbot.", "You can call me Chatty."]],
    [r"what can you do", ["I can chat with you! Try asking me something."]],
    [r"quit|exit", ["Goodbye!", "See you later!"]],
]

# Fallback responses
fallback_responses = [
    "I'm not sure I understand.",
    "Can you rephrase that?",
    "Interesting... tell me more.",
    "Let's talk about something else."
]

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess user input
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]

# Simple rule-based matching
def match_input(user_input):
    processed = " ".join(preprocess(user_input))
    for pattern, responses in pairs:
        if nltk.re.search(pattern, processed):
            return random.choice(responses)
    return random.choice(fallback_responses)

# Chat loop
def chat():
    print("Chatbot: Hi! Type 'quit' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ['quit', 'exit']:
            print("Chatbot: Goodbye!")
            break
        response = match_input(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
