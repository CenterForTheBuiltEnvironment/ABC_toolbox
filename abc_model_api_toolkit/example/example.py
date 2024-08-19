import os
from abc_model_api_toolkit.api_client import call_abc_model_api
from abc_model_api_toolkit.data_processor import output_json_to_csv


def run_abc(
    input_json_file,
    output_json_file,
    output_csv_file,
    api_url="https://fastabc-57h9n.ondigitalocean.app/abc",
):
    """
    Function to run ABC model with your input json file.
    """
    call_abc_model_api(input_json_file, output_json_file, api_url)
    output_json_to_csv(output_json_file, output_csv_file)


if __name__ == "__main__":

    # Set up file paths (Change these file path as you want)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_json_file = os.path.join(current_dir, "example_input.json")
    output_json_file = os.path.join(current_dir, "example_output.json")
    output_csv_file = os.path.join(current_dir, "example_output.csv")

    run_abc(
        input_json_file=input_json_file,
        output_json_file=output_json_file,
        output_csv_file=output_csv_file,
    )
