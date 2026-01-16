from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is running! Access via frontend form."

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    physics = request.form['physics']
    chemistry = request.form['chemistry']
    maths = request.form['maths']
    
    total = int(physics) + int(chemistry) + int(maths)
    percentage = total / 3
    
    result = f"""
    <h2>Result</h2>
    <p>Name: {name}</p>
    <p>Physics: {physics}</p>
    <p>Chemistry: {chemistry}</p>
    <p>Maths: {maths}</p>
    <p>Total: {total}</p>
    <p>Percentage: {percentage:.2f}%</p>
    <a href="http://localhost:3000">Back to Form</a>
    """
    return render_template_string(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
