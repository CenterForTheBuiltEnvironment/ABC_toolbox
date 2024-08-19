import argparse
import os
from api_client import call_abc_model_api
from data_processor import process_json #output_json_to_csv

def main():
    parser = argparse.ArgumentParser(description="Call ABC model API and handle JSON input/output.")
    parser.add_argument('input_file', help="Path to the JSON input file")
    parser.add_argument('-o', '--output_file', help="Path to save the output JSON", default=None)
    parser.add_argument('-c', '--csv_file', help="Path to save the output CSV", default=None)
    parser.add_argument('-t', '--timeout', type=int, help="Request timeout in seconds", default=10)
    parser.add_argument('--show_headers', action='store_true', help="Show response headers in the output")
    parser.add_argument('--url', help="API URL", default='https://fastabc-57h9n.ondigitalocean.app/abc')
    args = parser.parse_args()

    # Call the API and save the output JSON
    call_abc_model_api(args.input_file, args.output_file, args.url, args.timeout)

    # Get input file details
    input_dir = os.path.dirname(args.input_file)
    input_name, input_ext = os.path.splitext(os.path.basename(args.input_file))

    # Set default output paths if not specified
    args.output_file = args.output_file or os.path.join(input_dir, f"{input_name}_output{input_ext}")
    args.csv_file = args.csv_file or os.path.join(input_dir, f"{input_name}_output.csv")

    # Call the API and save the output JSON
    call_abc_model_api(args.input_file, args.output_file, args.url, args.timeout)

    # Process the CSV output if csv_file is specified
    process_json(args.output_file, csv_output=True, csv_file_path=args.csv_file)


if __name__ == '__main__':
    main()
