from website import create_app
import firebase_admin
import json
from firebase_admin import credentials, auth
from flask import Flask, request

app = create_app()

if __name__ == "__main__":
    app.run(port=8000, debug=True)
