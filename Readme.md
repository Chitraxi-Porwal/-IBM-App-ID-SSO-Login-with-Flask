🔐 IBM App ID SSO Login with Flask

This project demonstrates how to integrate Single Sign-On (SSO) using IBM Cloud App ID into a Flask web application. It uses the OpenID Connect (OIDC) flow to authenticate users and fetch profile information securely.

🌐 Features

🔑 IBM App ID-based SSO (OAuth 2.0 + OpenID Connect)
👤 Fetches user profile using access token
🔄 Login and Logout functionality
📁 .env file for secure credentials
🌟 Minimal, clean frontend using Jinja templates

📁 Project Structure

├── app.py                  # Main Flask application
├── .env                    # Environment variables (client ID, secret, etc.)
├── templates/
│   └── home.html           # Welcome page after login
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

🔧 Setup Instructions

1. 🔐 Create an IBM App ID Instance
Go to IBM Cloud.
Create a new App ID instance.
Navigate to: Manage Authentication > Authentication Settings:
Add your callback URL: http://localhost:5000/callback
(Optional) Enable and configure Facebook/Google login.

2. 🔑 Get OIDC Configuration
Go to your instance’s Overview section and find:
Client ID
Client Secret
Discovery URL (looks like: https://<region>.appid.cloud.ibm.com/oauth/v4/<tenant-id>/.well-known/openid-configuration)

3. 🖥️ Clone & Run Locally
git clone https://github.com/your-username/ibm-app-id-flask-sso.git 
cd ibm-app-id-flask-sso

4. 📦 Install Dependencies
Make sure you have Python 3.7+ installed.

pip install -r requirements.txt

5. 🧪 Setup Environment Variables
Create a .env file in the root directory:

CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
REDIRECT_URI=http://localhost:5000/callback
DISCOVERY_URL=https://<region>.appid.cloud.ibm.com/oauth/v4/<tenant-id>/.well-known/openid-configuration

6. ▶️ Run the Flask App

python app.py
Visit: http://localhost:5000

📄 Code Overview

Login Flow:
Redirects to IBM App ID login page via authorization_endpoint.
On successful login, IBM redirects back to /callback.
Flask exchanges the code for an access token.
Uses token to fetch user profile from userinfo_endpoint.

Templates:
home.html displays user's name and email once logged in.

🔒 Security Notes
Keep .env out of version control (.gitignore it).
Never expose your CLIENT_SECRET in frontend code or public repos.
For production, use HTTPS and set a static secret key (app.secret_key).

🚀 Deployment Options
You can deploy this project on platforms like:

Platform	Supports Python	Notes
Render	✅	Easy setup, great for Flask apps
Railway	✅	Fast deployment, GitHub integration
Heroku	✅	Legacy option, still widely used
IBM Cloud Code Engine	✅	Ideal for IBM-native deployments
Fly.io	✅	Global app deployment with private services

🧠 Learn More
📚 IBM App ID Docs
🔒 OpenID Connect
🐍 Flask Official Docs

🤝 Contributing
Pull requests and feedback are welcome!
Feel free to fork the project and submit improvements.