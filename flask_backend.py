"""
This module provides a Flask backend for handling requests and 
interacting with the AI and healthcare information services.

Functions:
    home(): Renders the home page.
    submit(): Handles form submissions, interacts with the AI model, 
              and retrieves healthcare provider information.
"""

import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ai import get_ai_response
from gethealthcare import get_healthcare_info

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        str: The rendered HTML of the home page.
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handles form submissions, interacts with the AI model, 
    and retrieves healthcare provider information.

    Returns:
        Response: A JSON response containing the AI 
        response and healthcare provider information, or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'inputText' not in data:
            return jsonify({'error': 'Invalid input'}), 400

        zip_code = data['inputText'].split(' ')[0]
        user_message = data['inputText']
        response = get_ai_response(user_message)

        if response.text.split(' ')[0] == "Sorry,":
            return jsonify({'response': response.text})

        providers = get_healthcare_info(str(zip_code), response.text)
        if hasattr(response, 'text'):  # Ensure response has a 'text' attribute
            return jsonify({'response': response.text + "\n" + providers})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    except Exception as e:
        logging.exception("An error occurred during the /submit request")
        return jsonify({'error': f"An error occurred: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)







