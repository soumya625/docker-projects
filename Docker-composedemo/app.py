from flask import Flask  # Import Flask
app = Flask(__name__)  # Create app instance

@app.route("/")
def hello():
    return "Hello from Dockerized Flask app!"  # This line is indented 4 spaces

if  __name__ == "__main__":
    # Indented 4 spaces from the if statement
    app.run(host="0.0.0.0", port=5000)