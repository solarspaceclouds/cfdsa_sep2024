from flask import Flask, render_template
import random
import os
app = Flask(__name__)

# List of quotes
quotes = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]

@app.route('/')
def index():
    # Select a random quote
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    # app.run(debug=True)

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
    
