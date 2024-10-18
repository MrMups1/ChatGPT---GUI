from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI-KEY")


# Route for root URL
@app.route('/')
def home():
    return "Welcome to the ChatGPT API!"

# Route to serve the HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')

    # Construct a prompt to give a sarcastic response to "Mups"
    prompt = f"You are ChatGPT and you've been asked to respond sarcastically. The user says: '{user_input}'. Your response must include sarcastic congratulations directed at 'Mups'."

    try:
        # Send the prompt to OpenAI's GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",  # or whichever engine you prefer
            prompt=prompt,
            max_tokens=60
        )

        # Extract and return the response
        ai_message = response.choices[0].text.strip()
        return jsonify({'response': ai_message})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
