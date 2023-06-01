"""
Dependencies
pip install -U Flask
pip install -U flask_cors


Test
http://127.0.0.1:5000/api/items
"""

from flask import Flask, jsonify, request
from flask_cors.extension import CORS
import os

app = Flask(__name__)

# Define a list of items for our API to manage
items = ["item 1", "item 2"]

# Define CORS
CORS(app, origins=["http://localhost:6006", "http://localhost:3000"]) # Change to the port you need
app.config['CORS HEADERS'] = 'Content-Type'

# Define a GET endpoint that returns all items
@app.route('/api/get-item', methods=['GET'])
def get_items():
    return jsonify(items)

# Define a POST endpoint that creates a new item
@app.route('/api/post-item', methods=['POST'])
def create_item():
    # Get the request data as a JSON object
    data = request.get_json()

    # Add the new item to the list
    items.append(data)

    # Return the new item as a JSON object
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))