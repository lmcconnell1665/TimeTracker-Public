# API key:  OTA3NzhfOTJiMjM2MTk4NjdhNDI2OGFmNmExNDA5ZDU2NzhlY2E=
# API secret:  MWU5NzU3Y2FkMjU0NGJjNzlmMmIwMTBmNTYwZTI3YzA=

import requests

def main():

    parameters = {
    "apiKey": "OTA3NzhfOTJiMjM2MTk4NjdhNDI2OGFmNmExNDA5ZDU2NzhlY2E=",
    "apiSecret": "MWU5NzU3Y2FkMjU0NGJjNzlmMmIwMTBmNTYwZTI3YzA="
    }

    response = requests.post("https://api.timeular.com/api/v2/developer/sign-in", parameters)

    # Print the status code of the response.
    # print(response.status_code)
    print(response.content)

if __name__ == "__main__":
    main()