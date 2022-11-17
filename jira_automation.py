# Template - coded on the fly, watch indentation!

import requests
import json

url = "https://lanasdet.atlassian.net//rest/api/2/issue"        # replace 'lanasdet' with your domain-name

headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json" 
        }

payload = json.dumps
        {
        fields" : {
            "project": 
            {
            "key" : "TTS"
            },
            "summary" : "AndroidOS v13 beta  - app crashes on Samsung device",        # arbitrary value
            "description" : "New payment feature crashes on Pixel 6 emulator using beta Android OS with Samsung skin",        # arbitrary value
            "issuetype" : {
            "name" : "Task"
            }
        }
    }
)

response = requests.post(url, headers=headers, data=payload, auth=("lanasdet@gmail.com", "somepassword123"))        # use your your own credentials

print(response.text)

# Sample Console Output:
# {"id" : "10001", "key" : "TTS-1", "self" : "https://lanasdet.atlassian.net/rest/api/2/issue/10001"}
