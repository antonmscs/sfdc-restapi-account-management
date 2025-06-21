# sfdc-restapi-account-management
SFDC REST API Account Management App

App uses Authorization Code Flow and requires setup in SFDC:
- Setup > Identity > OAuth and OpenID Connect Settings: Enable "Allow Authorization Code and Credentials Flows"
- Setup > Apps > External Client App Manager > Create and Set up an External Client App
- Pull DOMAIN_NAME from the URL of the SFDC instance (before .my.salesforce.com) 
- Pull CLIENT_ID, CLIENT_SECRET, REDIRECT_URI from the External Client App's OAuth settings

# Requirements 
Flask:
pip3 install flask

# Running
python.exe app.py

