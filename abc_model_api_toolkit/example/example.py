import os
from abc_model_api_toolkit.api_client import get_abc_model_api_results
from abc_model_api_toolkit.data_processor import output_json_to_csv


API_URL = "https://backend-384255928646.us-west1.run.app/abc"

# Set up file paths (Change these file path as you want)
current_dir = os.path.dirname(os.path.abspath(__file__))
input_json_file_path = os.path.join(current_dir, "example_input.json")
output_json_file_path = os.path.join(current_dir, "example_output.json")
output_csv_file_path = os.path.join(current_dir, "example_output.csv")

results = get_abc_model_api_results(input_file=input_json_file_path, output_file=output_json_file_path, api_url=API_URL)
output_json_to_csv(output_json_file_path=results, csv_file_path=output_csv_file_path)

# Check CSV data
import pandas as pd
example_csv = pd.read_csv(output_csv_file_path)
print(example_csv)