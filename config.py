# ----- YOUR SALESFORCE SETTINGS -----
# Load environment variables from a .env file (requires python-dotenv)
# 1. Install the python-dotenv package if you haven't already:
# pip install python-dotenv
# 2. Create a .env file in the same directory as this script with the following content:
# CLIENT_ID=your_client_id  
# CLIENT_SECRET=your_client_secret
# DOMAIN=your_salesforce_domain 
# REDIRECT_URI=your_callback_url

from dotenv import load_dotenv
load_dotenv()
import os
CLIENT_ID = os.getenv("CLIENT_ID",'')
CLIENT_SECRET = os.getenv("CLIENT_SECRET",'')
DOMAIN = os.getenv("DOMAIN", 'domain.my.salesforce.com')  
REDIRECT_URI = os.getenv("REDIRECT_URI", 'http://localhost:5000/callback')  # Must match the Connected App

AUTH_URL = f'https://' + DOMAIN + '/services/oauth2/authorize'
TOKEN_URL = f'https://' + DOMAIN + '/services/oauth2/token' 
SCOPES = 'api refresh_token'
API_VERSION = 'v60.0'
