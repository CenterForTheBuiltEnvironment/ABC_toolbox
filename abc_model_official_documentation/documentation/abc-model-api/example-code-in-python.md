# Example code in Python

{% tabs %}
{% tab title="Overview" %}
#### Python Script for API Interaction Using your JSON file

This Python script is designed to interact with ABC model API by sending your JSON input file and handling responses. It uses command line arguments to accept input parameters, making it highly customizable for different use cases without modifying the code directly. The script performs the following functions:

1. Reads a JSON file containing the input data.
2. Sends this data as a POST request to the API.
3. Processes the API's JSON response and optionally saves it to a file or prints it to the console.

**Dependencies**

* Python 3
* Standard libraries:
  * `json`: Utilized for parsing JSON data.
  * `argparse`: Helps in parsing command line arguments.
  * `logging`: Provides logging capabilities to output error and status messages.
  * `sys`: Used for system-specific parameters and functions, particularly for exiting the script upon encountering an error.
* `requests`: Used for making HTTP requests to the API.
{% endtab %}

{% tab title="Usage" %}
1.  **Installation of Dependencies:** Before running the script, ensure that the necessary libraries are installed using pip:

    ```bash
    pip install requests
    ```
2. **Command Line Arguments**:
   * `input_file`**(required)**: The path to the JSON input file.
   * `-o`, `--output_file`: The path where the output JSON should be saved. If not provided, the output will be saved in the same directory as an input file and printed to the console.
   * `-t`, `--timeout`: The timeout in seconds for the API request. Default is 10 seconds.
   * `--show_headers`: If included, the script will log the response headers.
   * `--url`: The API URL to which the request is sent. URL of ABC model API is "[**https://fastabc-57h9n.ondigitalocean.app/abc**](https://fastabc-57h9n.ondigitalocean.app/abc)".
3. **Running the Script:** The script can be executed from the command line by providing the necessary arguments. Below is an example. **Use your file path without the <>**.

```bash
python <your_python_script_name.py> <.../your_input.json> --output_file <.../your_output.json> --show_headers
```
{% endtab %}

{% tab title="Example code" %}
{% code title="post_to_abc_api.py" %}
```python
import requests
import json
import sys
import argparse
import logging
from typing import Optional, Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_json_file(file_path: str) -> str:
    """Read and return the content of the JSON input file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Error: File not found - {file_path}")
        sys.exit(1)
    except IOError as e:
        logging.error(f"Error: Unable to read file {file_path} - {e}")
        sys.exit(1)

def post_json_data(url: str, data: str, headers: Dict[str, str], timeout: int) -> requests.Response:
    """Send a POST request to the specified URL with the given data and headers."""
    try:
        return requests.post(url, data=data, headers=headers, timeout=timeout)
    except requests.exceptions.Timeout:
        logging.error(f"Error: The request timed out after {timeout} seconds.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")
        sys.exit(1)

def save_output(file_path: str, data: str) -> None:
    """Save the given data to the specified file."""
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        logging.info(f"Output has been saved to {file_path}")
    except IOError as e:
        logging.error(f"Error: Unable to write to file {file_path} - {e}")
        sys.exit(1)

def main() -> None:
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Call ABC model API and handle JSON input/output.")
    parser.add_argument('input_file', help="Path to the JSON input file")
    parser.add_argument('-o', '--output_file', help="Path to save the output JSON", default=None)
    parser.add_argument('-t', '--timeout', type=int, help="Request timeout in seconds", default=10)
    parser.add_argument('--show_headers', action='store_true', help="Show response headers in the output")
    parser.add_argument('--url', help="API URL", default='https://fastabc-57h9n.ondigitalocean.app/abc')
    args = parser.parse_args()

    # Read the input file
    input_text = read_json_file(args.input_file)

    # Set headers for JSON
    headers = {'Content-Type': 'application/json'}

    # Send the POST request
    response = post_json_data(args.url, input_text, headers, args.timeout)

    # Check the response status code
    if response.status_code == 200:
        # Optionally show response headers
        if args.show_headers:
            logging.info("Response Headers:")
            for key, value in response.headers.items():
                logging.info(f"{key}: {value}")

        # Process the JSON response
        pretty = json.dumps(response.json(), indent=2)
        if args.output_file:
            save_output(args.output_file, pretty)
        else:
            print(pretty)
    else:
        logging.error(f'Response error: {response.status_code}')
        logging.error(response.text)

if __name__ == '__main__':
    main()
```
{% endcode %}
{% endtab %}
{% endtabs %}

We provide a Python script to interact with ABC model API by sending your JSON input file and handling responses. Please visit this GitHub repository.

{% embed url="https://vimeo.com/943333333" %}
