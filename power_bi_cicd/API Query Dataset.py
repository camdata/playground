import msal
import requests
import json
import pandas

# --------------------------------------------------
# Set local variables
# --------------------------------------------------
client_id=
username = 
password = 
authority_url = 
scope = ["https://analysis.windows.net/powerbi/api/.default"]
url_groups = 

# --------------------------------------------------
# Use MSAL to grab a token
# --------------------------------------------------
app = msal.PublicClientApplication(client_id, authority=authority_url)
result = app.acquire_token_by_username_password(scopes=scope, username = username, password=password)

# --------------------------------------------------
# Check if a token was obtained, grab it and call the
# Power BI REST API, otherwise throw up the error message
# --------------------------------------------------

access_token = result['access_token']
header = {'Authorization': f'Bearer {access_token}','Content-Type': 'application/json'}
refresh_url = ''
body = "{\"queries\": [{\"query\": \"EVALUATE 'Line Item '\"}]}"
r = requests.post(url=refresh_url, headers=header,data=body)
r
r.text
