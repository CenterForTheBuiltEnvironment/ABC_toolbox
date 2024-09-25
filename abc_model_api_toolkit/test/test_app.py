import requests
import json

# URL of the Flask API
url = "http://localhost:5000/convert-file"

# JSON payload with the file path
payload = {
    "json_file_path": "C:\\Users\\monyo\\PycharmProjects\\ABC_JSON_schema\\abc_model_api_toolkit\\example\\example_output.json"
}

# Send POST request to the Flask API
response = requests.post(url, json=payload)

# Print the response from the server
print(response.json())
