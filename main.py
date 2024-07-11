import os
from flask import Flask, redirect, request

app = Flask(__name__)

# Get the redirect domain from an environment variable
REDIRECT_DOMAIN = os.getenv('REDIRECT_DOMAIN', 'https://google.com')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    full_path = request.full_path
    redirect_url = f'{REDIRECT_DOMAIN}{full_path}'
    return redirect(redirect_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)