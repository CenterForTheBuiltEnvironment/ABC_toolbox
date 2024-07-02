import argparse
from abc_model_api_client import call_abc_model_api
from data_processor import output_json_to_csv

def main():
    parser = argparse.ArgumentParser(description="Call ABC model API and handle JSON input/output.")
    parser.add_argument('input_file', help="Path to the JSON input file")
    parser.add_argument('-o', '--output_file', help="Path to save the output JSON", default=None)
    parser.add_argument('-c', '--csv_file', help="Path to save the output CSV", default=None)
    parser.add_argument('-t', '--timeout', type=int, help="Request timeout in seconds", default=10)
    parser.add_argument('--show_headers', action='store_true', help="Show response headers in the output")
    parser.add_argument('--url', help="API URL", default='https://fastabc-57h9n.ondigitalocean.app/abc')
    args = parser.parse_args()

    output_file = args.output_file or 'output.json'
    call_abc_model_api(args.input_file, output_file, args.url, args.timeout)

    if args.csv_file:
        output_json_to_csv(output_file, args.csv_file)

if __name__ == '__main__':
    main()
