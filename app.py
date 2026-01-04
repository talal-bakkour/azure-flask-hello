import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    msg = os.getenv("APP_MESSAGE", "Hello from Azure App Service 🚀")
    return f"""
    <h1>{msg}</h1>
    <p>This is a Flask app deployed on Azure.</p>
    """
