import secrets
import string
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Serves the main HTML webpage
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Fetch the length from the incoming request data
    data = request.get_json()
    length = int(data.get('length', 12))
    
    # Define pools matching your requirements (letters + numbers)
    letters = string.ascii_letters
    digits = string.digits
    all_chars = letters + digits
    
    # Guarantee at least one letter and one number
    password_list = [
        secrets.choice(letters),
        secrets.choice(digits)
    ]
    
    # Fill up the rest of the requested length
    for _ in range(length - 2):
        password_list.append(secrets.choice(all_chars))
        
    # Shuffle securely to mix the guaranteed characters away from the front
    secrets.SystemRandom().shuffle(password_list)
    password = "".join(password_list)
    
    # Return the password back to the HTML page instantly
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)