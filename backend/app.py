from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client['todoapp']
todos = db['todos']

@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    data = {
        'itemName': request.form['itemName'],
        'itemDescription': request.form['itemDescription'],
        'created_at': datetime.utcnow()
    }
    todo_id = todos.insert_one(data).inserted_id
    return f"To-Do created with ID: {str(todo_id)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
