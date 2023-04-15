

import msal
import requests
import json
import pandas
import datetime

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
header = {'Authorization': f'Bearer {access_token}'}
workspace_url = 'https://api.powerbi.com/v1.0/myorg/groups'
workspaces = requests.get(url=workspace_url, headers=header)

## Get list of workspaces and detaisl account had access to
## GET https://api.powerbi.com/v1.0/myorg/groups

## Get list of datasets and their detaisl from workspace
## GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets



workspace_dict = workspaces.json()
workspace_recs = workspace_dict['value']
workspace_df = pandas.json_normalize(workspace_recs)

workspace_name = 'Athena Data \[Dev\]'
dev_workspace = workspace_df[workspace_df['name'].str.contains(workspace_name)]

dev_workspace_id = dev_workspace["id"].values[0]

get_datasets_url = 'https://api.powerbi.com/v1.0/myorg/groups/' + dev_workspace_id + '/datasets'
dataset = requests.get(url=get_datasets_url, headers=header)


dataset_dict = dataset.json()
dataset_recs = dataset_dict['value']
dataset_df = pandas.json_normalize(dataset_recs)


##print json
##json_object = json.loads(dataset.text)
##print(json.dumps(json_object, indent = 1))

dataset_name = 
dev_dataset = dataset_df[dataset_df['name'].str.contains(dataset_name)]
dev_dataset_id = dev_dataset["id"].values[0]

## get latest dataset refresh
##GET https://api.powerbi.com/v1.0/myorg/datasets/{datasetId}/refreshes?$top={$top}


url_get_refresh = 'https://api.powerbi.com/v1.0/myorg/datasets/' + dev_dataset_id + '/refreshes?$top=1'
refreshes = requests.get(url=url_get_refresh, headers=header)

refresh_dict = refreshes.json()
refresh_recs = refresh_dict['value']
refresh_df = pandas.json_normalize(refresh_recs)

last_refresh = refresh_df["startTime"].values[0]

##time comparison
time = datetime.datetime.strptime(last_refresh[0:-1],"%Y-%m-%dT%H:%M:%S.%f")
diff = datetime.datetime.utcnow() -  time
delta = diff.total_seconds()
##hours from last run
delta/3600