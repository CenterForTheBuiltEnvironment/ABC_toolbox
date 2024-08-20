# Example code in Python

{% @github-files/github-code-block %}

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
{% @github-files/github-code-block url="https://github.com/CenterForTheBuiltEnvironment/ABC_toolbox/blob/main/abc_model_api_toolkit/example/example.py" %}
{% endtab %}
{% endtabs %}
