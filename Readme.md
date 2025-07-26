# IBM App ID SSO Login with Flask <br/>
This project demonstrates how to integrate Single Sign-On (SSO) using IBM Cloud App ID into a Flask web application. It uses the OpenID Connect (OIDC) flow to authenticate users and fetch profile information securely.

## Features <br/>
🔑 IBM App ID-based SSO (OAuth 2.0 + OpenID Connect) <br/>
👤 Fetches user profile using access token <br/>
🔄 Login and Logout functionality <br/>
📁 .env file for secure credentials <br/>
🌟 Minimal, clean frontend using Jinja templates <br/>

## Project Structure  <br/>
├── app.py               &ensp;    # Main Flask application  <br/>
├── .env                &ensp;     # Environment variables (client ID, secret, etc.)   <br/>
├── templates/                                                                  <br/>
 |    &ensp; &ensp;     └── home.html       &nbsp;     # Welcome page after login                    <br/>
├── requirements.txt     &ensp;    # Python dependencies                               <br/>
└── README.md           &ensp;     # Project documentation                            <br/>

## Setup Instructions <br/>
1. 🔐 Create an IBM App ID Instance <br/>
Go to IBM Cloud.<br/>
Create a new App ID instance.<br/>
Navigate to: Manage Authentication > Authentication Settings:<br/>
Add your callback URL: http://localhost:5000/callback     <br/>
(Optional) Enable and configure Facebook/Google login.   <br/>

2. 🔑 Get OIDC Configuration    <br/>
Go to your instance’s Overview section and find:  <br/>
Client ID<br/>
Client Secret<br/>
Discovery URL (looks like: https://<region>.appid.cloud.ibm.com/oauth/v4/<tenant-id>/.well-known/openid-configuration)<br/>

3. 🖥️ Clone & Run Locally<br/>
git clone https://github.com/your-username/ibm-app-id-flask-sso.git<br/>
cd ibm-app-id-flask-sso<br/>

4. 📦 Install Dependencies<br/>
Make sure you have Python 3.7+ installed.<br/>
pip install -r requirements.txt<br/>

5. 🧪 Setup Environment Variables<br/>
Create a .env file in the root directory:<br/>
CLIENT_ID=your-client-id<br/>
CLIENT_SECRET=your-client-secret<br/>
REDIRECT_URI=http://localhost:5000/callback<br/>
DISCOVERY_URL=https://<region>.appid.cloud.ibm.com/oauth/v4/<tenant-id>/.well-known/openid-configuration<br/>

6. ▶️ Run the Flask App<br/>
python app.py<br/>
Visit: http://localhost:5000<br/>

## Code Overview

Login Flow:<br/>
Redirects to IBM App ID login page via authorization_endpoint.<br/>
On successful login, IBM redirects back to /callback.<br/>
Flask exchanges the code for an access token.<br/>
Uses token to fetch user profile from userinfo_endpoint.<br/>

Templates:<br/>
home.html displays user's name and email once logged in.<br/>

## Security Notes
Keep .env out of version control (.gitignore it).<br/>
Never expose your CLIENT_SECRET in frontend code or public repos.<br/>
For production, use HTTPS and set a static secret key (app.secret_key).<br/>

## Deployment Options
You can deploy this project on platforms like:<br/>

Platform	Supports Python	Notes<br/>
Render	✅	Easy setup, great for Flask apps<br/>
Railway	✅	Fast deployment, GitHub integration<br/>
Heroku	✅	Legacy option, still widely used<br/>
IBM Cloud Code Engine	✅	Ideal for IBM-native deployments<br/>
Fly.io	✅	Global app deployment with private services<br/>

## Learn More
📚 IBM App ID Docs<br/>
🔒 OpenID Connect<br/>
🐍 Flask Official Docs<br/>

## Contributing
Pull requests and feedback are welcome!<br/>
Feel free to fork the project and submit improvements.<br/>

