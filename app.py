from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['my_db']
collection = db['user_data']

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    collection.insert_one({'name': name, 'email': email})
    return jsonify({'message': 'Data submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
