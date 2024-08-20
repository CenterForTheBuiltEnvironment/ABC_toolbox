# Example code in Python

{% tabs %}
{% tab title="Overview" %}
**abc\_model\_api\_toolkit**

We provide an example Python script to interact with ABC model API. Please check the details at ABC\_

{% @github-files/github-code-block url="https://github.com/CenterForTheBuiltEnvironment/ABC_toolbox/tree/main/abc_model_api_toolkit" %}

You can use command line arguments to accept input parameters or your Python script. The script performs the following functions:

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

{% tab title="Example code" %}
{% @github-files/github-code-block url="https://github.com/CenterForTheBuiltEnvironment/ABC_toolbox/blob/main/abc_model_api_toolkit/example/example.py" %}
{% endtab %}
{% endtabs %}
