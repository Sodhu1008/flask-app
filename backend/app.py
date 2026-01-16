from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

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
