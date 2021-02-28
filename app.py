# Import Statements
from flask import Flask, render_template

# Create the Flask App
app = Flask(__name__)

# Create the index route
@app.route('/')
def index():
    return render_template('index.html')

# Run the Application
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')