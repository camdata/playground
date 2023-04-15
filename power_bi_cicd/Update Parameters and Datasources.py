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
scope = 
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


#Take Over Dataset
url =  ""
r = requests.post(url=url, headers=header)

#Update Parameter
refresh_url = ''
body = "{\"updateDetails\": [{\"name\": \"DataStart\",\"newValue\": \"20001231\"}]}"
r = requests.post(url=refresh_url, headers=header,data=body)
r


#--------------------------------------

#Update Datasource
#Take Over Dataset
url =  ""
r = requests.post(url=url, headers=header)

#Set DataSource
url =  ""
body = 
body2 = 
r = requests.post(url=refresh_url, headers=header,data=body)


#Get Datasrouce Type
url =  
r = requests.get(url=url, headers=header)



