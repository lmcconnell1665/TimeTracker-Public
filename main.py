"""
Time Tracker
Connected to the Timeular API and returns data
Luke McConnell
"""
import json
from datetime import datetime, timedelta
import requests

def main():
    """
    interacts with the Timeular API to gather time tracking data.
    """

    parameters = {
        "apiKey": "OTA3NzhfZmI5M2U1MjFjMzkyNDk2MmIzMjkyNjViNWI1OWE4NDE=",
        "apiSecret": "ZjZmOTRiNzUzNDAxNGRlYmEyZjcxZWI4MTg1Y2EzMDM="
    }

    auth_token = fetch_token(parameters)

    data = fetch_data(auth_token)
    data_dict = json.loads(data)
    print(data_dict)

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

def fetch_data(token):
    """
    gets all of the data for the last 90 days
    """

    bearer_token = json.loads(token)

    today = datetime.now()
    ninty_days_ago = today - timedelta(days=90)
    new_format = "%Y-%m-%dT%H:%M:%S.%f"

    now = today.strftime(new_format)[:-3]
    ago = ninty_days_ago.strftime(new_format)[:-3]

    url = 'https://api.timeular.com/api/v3/report/data/' + ago + '/' + now

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(bearer_token['token'])
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text.encode('utf8')

if __name__ == "__main__":
    main()
