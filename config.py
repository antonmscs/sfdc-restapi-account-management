# ----- YOUR SALESFORCE SETTINGS -----
CLIENT_ID = '' # Replace with your actual client ID
CLIENT_SECRET = ''  # Replace with your actual client secret
DOMAIN = ''  # Replace with your actual Salesforce domain 
REDIRECT_URI = 'http://localhost:5000/callback'  # Must match the Connected App
AUTH_URL = f'https://' + DOMAIN + '/services/oauth2/authorize'
TOKEN_URL = f'https://' + DOMAIN + '/services/oauth2/token' 
SCOPES = 'api refresh_token'
API_VERSION = 'v60.0'