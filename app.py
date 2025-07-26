import os
import requests
from flask import Flask, redirect, request, session, url_for, render_template
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ENV
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
DISCOVERY_URL = os.getenv("DISCOVERY_URL")

# Fetch OIDC Configuration
oidc_config = requests.get(DISCOVERY_URL).json()
AUTH_URL = oidc_config["authorization_endpoint"]
TOKEN_URL = oidc_config["token_endpoint"]
USERINFO_URL = oidc_config["userinfo_endpoint"]

@app.route('/')
def home():
    if 'user' in session:
        return render_template("home.html", user=session['user'])
    return '<a href="/login">Login with IBM App ID</a>'

@app.route('/login')
def login():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "openid profile"
    }
    return redirect(f"{AUTH_URL}?{urlencode(params)}")

@app.route('/callback')
def callback():
    code = request.args.get("code")
    if not code:
        return "Authorization failed.", 400

    # Exchange code for access token
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    token_response = requests.post(TOKEN_URL, data=data, headers=headers)
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    # Get user info
    userinfo_response = requests.get(USERINFO_URL, headers={"Authorization": f"Bearer {access_token}"})
    session['user'] = userinfo_response.json()

    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
