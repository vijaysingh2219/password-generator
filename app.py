# Import necessary modules
from flask import Flask, render_template, request
import random
import string

# Create a Flask web application instance
app = Flask(__name__)


def generate_password(length=16, include_digits=True, include_letters=True, include_symbols=False):
    """
    Generate a random password based on specified criteria.

    Parameters:
    - length (int): Length of the password.
    - include_digits (bool): Include digits in the password.
    - include_letters (bool): Include letters (both uppercase and lowercase) in the password.
    - include_symbols (bool): Include special symbols in the password.

    Returns:
    - str: Generated password.
    """
    characters = ''
    if include_digits:
        characters += string.digits
    if include_letters:
        characters += string.ascii_letters
    if include_symbols:
        characters += '@&$!#?'

    password = ''.join(random.choice(characters) for i in range(length))
    return password


# Define route for the home page
@app.route('/')
def index():
    """
    Render the home page.

    Returns:
    - Flask.Response: Rendered HTML template with default password generation settings.
    """
    return render_template('index.html', length=16, include_digits=True, include_letters=True, include_symbols=False)


# Define route for password generation based on user input
@app.route('/generate_password', methods=['POST'])
def generate():
    """
    Handle password generation based on user input.

    Returns:
    - Flask.Response: Rendered HTML template with the generated password and user input settings.
    """
    length = int(request.form.get('length', 16))
    include_digits = 'include_digits' in request.form
    include_letters = 'include_letters' in request.form
    include_symbols = 'include_symbols' in request.form

    password = generate_password(
        length, include_digits, include_letters, include_symbols)

    return render_template('index.html', password=password, length=length,
                           include_digits=include_digits, include_letters=include_letters, include_symbols=include_symbols)


# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
