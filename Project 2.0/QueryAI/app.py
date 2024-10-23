from flask import Flask, request, jsonify
import openai  # Ensure you have the OpenAI library installed

app = Flask(__name__)  # Corrected the variable name from _name_ to __name__

# Add your OpenAI API key here (if using OpenAI)
openai.api_key = 'your-openai-api-key'

@app.route('/get-answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data.get('question')

    if not question:  # Check if the question is not empty
        return jsonify({'error': 'No question provided'}), 400

    # Call to OpenAI API (you can also use your own AI model)
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 engine
        prompt=question,
        max_tokens=50
    )

    answer = response['choices'][0]['text'].strip()

    return jsonify({'answer': answer})

if __name__ == '__main__':  # Corrected the variable name from _name_ to __name__
    app.run(debug=True)
