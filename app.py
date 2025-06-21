import webbrowser
import requests
import db

from flask import Flask, jsonify, redirect, render_template, request, session
from urllib.parse import urlencode

# Import your configuration module 
import config 

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')    
    return html

@app.route('/authenticate', methods=['GET'])
def authenticate():
    # ----- STEP 1: Build the authorization URL -----
    params = {
        'response_type': 'code',
        'client_id': config.CLIENT_ID,
        'redirect_uri': config.REDIRECT_URI,
        'scope': config.SCOPES
    }
    
    auth_request_url = f"{config.AUTH_URL}?{urlencode(params)}"

    # Navigate the user to the authorization URL
    ##webbrowser.open(auth_request_url)
    
    ##return jsonify({'message': 'Authentication started!'})

    #return redirect(auth_request_url)
    return f"""
    <html>
    <head><title>Redirecting...</title></head>
    <body>
        <p>Redirecting to authentication provider, please wait...</p>
        <script>
            window.location.href = "{auth_request_url}";
        </script>
    </body>
    </html>
    """



@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "No code received!", 400

    # Exchange code for tokens
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET,
        'redirect_uri': config.REDIRECT_URI
    }
    token_resp = requests.post(config.TOKEN_URL, data=token_data)
    if not token_resp.ok:
        return f"Token request failed: {token_resp.text}", 400

    tokens = token_resp.json()
    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token')
    instance_url = tokens['instance_url']
    db.save_session(access_token, instance_url)
    
    # Print tokens in the console
    print("\n=== OAUTH TOKENS RECEIVED ===")
    print(tokens)    
    
    return """
<html>
<head><title>Authenticated</title></head>
<body>
    <p>Authentication Successful! You may now close this window.</p>
    <script>
        if (window.opener) {
            window.opener.document.getElementById('auth-status').textContent = 'Authentication Successful';
        }
    </script>
</body>
</html>
"""

@app.route('/search', methods=['POST'])
def search():
    print("\n=== /SEARCH ===")
    '''
    if 'access_token' not in session:
        return jsonify({
            'code': 401,
            'message': 'You need to authenticate first.',
        })
    '''
    get_sessions = db.get_sessions()
    access_token = get_sessions[0]['access_token'] if get_sessions else None
    instance_url = get_sessions[0]['instance_url'] if get_sessions else None
    print("Access Token:", access_token)
    print("Instance URL:", instance_url)

    # ---- Query Accounts ----
    accounts_url = f"{instance_url}/services/data/{config.API_VERSION}/query"
    
    # Query to return first account that contains the word "Test"
    soql_query = "SELECT Id, Name FROM Account WHERE Name LIKE '%United%' LIMIT 1"    
    params = {'q': soql_query}

    headers = { 
        "Authorization": f"Bearer {access_token}"
    }

    accounts_response = requests.get(accounts_url, headers=headers, params=params)
    accounts_response.raise_for_status()  # Will throw error if something goes wrong

    accounts = accounts_response.json()
    
    print("\n=== ACCOUNTS QUERY RESPONSE ===")
    print(accounts)
    
    if(accounts['totalSize'] == 0):
        # No accounts found
        return jsonify({
            'code': 200,
            'message': 'No accounts found with the specified criteria.'
        })
    
    return jsonify({
        'code': 200,
        'message': 'Account found: ' + accounts['records'][0]['Name'],        
    })


if __name__ == '__main__':
    app.run()   