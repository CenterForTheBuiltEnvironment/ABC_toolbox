import requests
import json
import sys

def send_request(url, input_file):
    """Send a POST request to the specified URL with data loaded from a JSON input file."""
    try:
        with open(input_file, 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f'Error: The file {input_file} could not be found.')
        sys.exit()

    response = requests.post(url, data=input_text)

    if response.status_code == 200:
        pretty_output = json.dumps(response.json(), indent=2)
        print(pretty_output)
    else:
        print('Response error:', response.status_code)
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input JSON filename>")
        sys.exit()

    url = 'https://fastabc-57h9n.ondigitalocean.app/abc'
    input_filename = sys.argv[1]
    send_request(url, input_filename)
