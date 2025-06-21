# sfdc-restapi-account-management
SFDC REST API Account Management App

App uses Authorization Code Flow and requires setup in SFDC:
- Setup > Identity > OAuth and OpenID Connect Settings: Enable "Allow Authorization Code and Credentials Flows"
- Setup > Apps > External Client App Manager > Create and Set up an External Client App
- Pull DOMAIN_NAME from the URL of the SFDC instance (before .my.salesforce.com) 
- Pull CLIENT_ID, CLIENT_SECRET, REDIRECT_URI from the External Client App's OAuth settings (for running it locally set Call Back URL in OAuth settings to http://localhost:5000/callback)

sqlite3 database is used to store access token and instance_url returned by SFDC after authentication

# Requirements 
Flask:
pip3 install flask

python-dotenv:
pip3 install python-dotenv

# Running
python.exe app.py

# ToDo
Modify a query to return the latest session
Need to maintain only current session in the database instead or adding new values after each authorization
