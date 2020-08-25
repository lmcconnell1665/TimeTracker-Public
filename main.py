"""
Time Tracker
Connected to the Timeular API and returns data
Luke McConnell
"""
import json
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

    activities = fetch_activities(auth_token)
    activities_dict = json.loads(activities)
    print(activities_dict)

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

def fetch_activities(token):
    """
    gets all of the activities for the account.
    """

    bearer_token = json.loads(token)

    url = "https://api.timeular.com/api/v3/activities"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + str(bearer_token['token'])
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text.encode('utf8')

if __name__ == "__main__":
    main()
