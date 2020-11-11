"""
Time Tracker
Connected to the Timeular API and returns data
Luke McConnell
"""
import json
from datetime import datetime, timedelta
import requests
import pandas as pd
from decouple import config

def main():
    """
    interacts with the Timeular API to gather time tracking data.
    """

    key = config('API_KEY')
    secret = config('API_SECRET')

    parameters = {
        "apiKey": key,
        "apiSecret": secret
    }

    # fctEntries
    auth_token = fetch_token(parameters) # gets the authorization token
    data = fetch_data(auth_token, 'fctEntries') # fetches the data
    data_dict = json.loads(data) # creates a dict from the json payload
    fct_entries = generate_entries_df(data_dict) # creates a dataframe and adds a duration calculation

    # # dimActivities
    auth_token = fetch_token(parameters) # gets the authorization token
    data = fetch_data(auth_token, 'dimActivities') # fetches the data
    data_dict = json.loads(data) # creates a dict from the json payload
    dim_activities = generate_activities_df(data_dict) # creates a dataframe

    # # dimTags
    auth_token = fetch_token(parameters) # gets the authorization token
    data = fetch_data(auth_token, 'dimTags') # fetches the data
    data_dict = json.loads(data) # creates a dict from the json payload
    dim_tags = generate_tags_df(data_dict)

    # Insert tags into entry notes

    # Save dataframe as csv
    date = datetime.now()

    fct_entries.to_csv("fct_entries.csv", index=False)
    # dim_activities.to_csv("dim_activities"+str(date)+".csv", index=False)
    # dim_tags.to_csv("dim_tags"+str(date)+".csv", index=False)
    print ("done")
    return 'Done'

def fetch_token(account_parameters):
    """
    sends a POST request to the url and returns an authorization token.
    """

    url = "https://api.timeular.com/api/v3/developer/sign-in"

    payload = "{\"apiKey\" : \"" + account_parameters['apiKey'] + "\", \"apiSecret\" : \"" + account_parameters['apiSecret'] + "\"}"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    token = (response.text.encode('utf8'))

    return token.decode('UTF-8')

def fetch_data(token, which_data):
    """
    gets all of the data for the last 90 days
    """

    bearer_token = json.loads(token)

    if which_data == 'fctEntries':

        today = datetime.now()
        ninty_days_ago = today - timedelta(days=120)
        new_format = "%Y-%m-%dT%H:%M:%S.%f"

        now = today.strftime(new_format)[:-3]
        ago = ninty_days_ago.strftime(new_format)[:-3]

        url = 'https://api.timeular.com/api/v3/time-entries/' + ago + '/' + now

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(bearer_token['token'])
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.text.encode('utf8')

    elif which_data == 'dimActivities':

        url = "https://api.timeular.com/api/v3/activities"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(bearer_token['token'])
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.text.encode('utf8')

    elif which_data == 'dimTags':

        url = "https://api.timeular.com/api/v3/tags-and-mentions"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + str(bearer_token['token'])
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.text.encode('utf8')

    return data

def generate_entries_df(payload):
    """
    Converts the json data into a pandas dataframe
    """
    original_list = []
    for i in range(len(payload['timeEntries'])):
        new_item = {'id' : payload['timeEntries'][i]['id'],
                    'activityId' :  payload['timeEntries'][i]['activityId'],
                    'startTime' : payload['timeEntries'][i]['duration']['startedAt'],
                    'endTime' : payload['timeEntries'][i]['duration']['stoppedAt'],
                    'note' : payload['timeEntries'][i]['note']['text']}
        original_list.append(new_item)

    data_frame = pd.DataFrame(original_list)

    new_format = "%Y-%m-%dT%H:%M:%S.%f"

    for i in range(len(payload['timeEntries'])):
        data_frame.loc[i, 'duration'] = \
            datetime.strptime(data_frame['endTime'][i], new_format) \
            - datetime.strptime(data_frame['startTime'][i], new_format)

    data_frame = data_frame[['id', 'activityId', 'startTime', 'endTime', 'duration', 'note']]

    return data_frame

def generate_activities_df(payload):
    """
    Converts the json data into a pandas dataframe
    """
    original_list = []

    for i in range(len(payload['activities'])):
        new_item = {'id' : payload['activities'][i]['id'],
                    'name' : payload['activities'][i]['name'],
                    'color' : payload['activities'][i]['color'],
                    'deviceSide' : payload['activities'][i]['deviceSide']}
        original_list.append(new_item)

    data_frame = pd.DataFrame(original_list)

    return data_frame

def generate_tags_df(payload):
    """
    Converts the json data into a pandas dataframe
    """
    original_list = []

    for i in range(len(payload['tags'])):
        new_item = {'id' : payload['tags'][i]['id'],
                    'key' : payload['tags'][i]['key'],
                    'label' : payload['tags'][i]['label']}
        original_list.append(new_item)

    data_frame = pd.DataFrame(original_list)

    data_frame = data_frame[['id', 'label', 'key']]

    return data_frame

if __name__ == "__main__":
    main()
