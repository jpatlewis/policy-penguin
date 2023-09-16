from flask import Flask
from app.app import create_app  # Import the create_app function

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
