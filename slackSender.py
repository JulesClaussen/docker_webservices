import requests
import sys

url = "https://hooks.slack.com/services/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"

payload = "{\r\n    \"text\": \sys.argv[1]\r\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "f7f5d4a0-8b39-4283-9806-67f233e54468"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)