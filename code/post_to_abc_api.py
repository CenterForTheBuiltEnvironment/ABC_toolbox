# import requests
# import json
# import csv
# import sys
# import argparse
# import logging
# from typing import Optional, Dict, Any
#
# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def read_json_file(file_path: str) -> str:
#     """Read and return the content of the JSON input file."""
#     try:
#         with open(file_path, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         logging.error(f"Error: File not found - {file_path}")
#         sys.exit(1)
#     except IOError as e:
#         logging.error(f"Error: Unable to read file {file_path} - {e}")
#         sys.exit(1)
#
# def post_json_data(url: str, data: str, headers: Dict[str, str], timeout: int) -> requests.Response:
#     """Send a POST request to the specified URL with the given data and headers."""
#     try:
#         return requests.post(url, data=data, headers=headers, timeout=timeout)
#     except requests.exceptions.Timeout:
#         logging.error(f"Error: The request timed out after {timeout} seconds.")
#         sys.exit(1)
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error: {e}")
#         sys.exit(1)
#
# def save_output(file_path: str, data: str) -> None:
#     """Save the given data to the specified file."""
#     try:
#         with open(file_path, 'w') as file:
#             file.write(data)
#         logging.info(f"Output has been saved to {file_path}")
#     except IOError as e:
#         logging.error(f"Error: Unable to write to file {file_path} - {e}")
#         sys.exit(1)
#
#
# def output_json_to_csv(output_json_file_path, csv_file_path):
#     """
#     Converts a JSON file to a CSV file based on the specific format.
#
#     Parameters:
#     json_file_path (str): The path to the input JSON file.
#     csv_file_path (str): The path to the output CSV file.
#     """
#     # Load the JSON data
#     with open(output_json_file_path) as json_file:
#         data = json.load(json_file)
#
#     # Extract headers from the first segment
#     first_result = data['results'][0]
#     overall_headers = ['time', 'met', 'clo_ensemble_name', 'clo'] + list(first_result['overall'].keys())
#     segment_headers = list(first_result['segments']['Head'].keys())
#     headers = overall_headers + ['segment'] + segment_headers
#
#     # Write data to CSV
#     with open(csv_file_path, mode='w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(headers)
#
#         for result in data['results']:
#             overall_data = [result['time'], result['met'], result['clo_ensemble_name'], result['clo']] + list(
#                 result['overall'].values())
#             for segment, segment_data in result['segments'].items():
#                 row = overall_data + [segment] + list(segment_data.values())
#                 writer.writerow(row)
#
#     print(f"Data successfully written to {csv_file_path}")
#
# def main() -> None:
#     # Set up argument parsing
#     parser = argparse.ArgumentParser(description="Call ABC model API and handle JSON input/output.")
#     parser.add_argument('input_file', help="Path to the JSON input file")
#     parser.add_argument('-o', '--output_file', help="Path to save the output JSON", default=None)
#     parser.add_argument('-t', '--timeout', type=int, help="Request timeout in seconds", default=10)
#     parser.add_argument('--show_headers', action='store_true', help="Show response headers in the output")
#     parser.add_argument('--url', help="API URL", default='https://fastabc-57h9n.ondigitalocean.app/abc')
#     args = parser.parse_args()
#
#     # Read the input file
#     input_text = read_json_file(args.input_file)
#
#     # Set headers for JSON
#     headers = {'Content-Type': 'application/json'}
#
#     # Send the POST request
#     response = post_json_data(args.url, input_text, headers, args.timeout)
#
#     # Check the response status code
#     if response.status_code == 200:
#         # Optionally show response headers
#         if args.show_headers:
#             logging.info("Response Headers:")
#             for key, value in response.headers.items():
#                 logging.info(f"{key}: {value}")
#
#         # Process the JSON response
#         pretty = json.dumps(response.json(), indent=2)
#         if args.output_file:
#             save_output(args.output_file, pretty)
#         else:
#             print(pretty)
#     else:
#         logging.error(f'Response error: {response.status_code}')
#         logging.error(response.text)
#
# if __name__ == '__main__':
#     main()
import requests
import json
import csv
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


def output_json_to_csv(output_json_file_path, csv_file_path):
    """
    Converts a JSON file to a CSV file based on the specific format.

    Parameters:
    json_file_path (str): The path to the input JSON file.
    csv_file_path (str): The path to the output CSV file.
    """
    # Load the JSON data
    with open(output_json_file_path) as json_file:
        data = json.load(json_file)

    # Extract headers from the first segment
    first_result = data['results'][0]
    overall_headers = ['time', 'met', 'clo_ensemble_name', 'clo'] + list(first_result['overall'].keys())
    segment_headers = list(first_result['segments']['Head'].keys())
    headers = overall_headers + ['segment'] + segment_headers

    # Write data to CSV
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for result in data['results']:
            overall_data = [result['time'], result['met'], result['clo_ensemble_name'], result['clo']] + list(
                result['overall'].values())
            for segment, segment_data in result['segments'].items():
                row = overall_data + [segment] + list(segment_data.values())
                writer.writerow(row)

    print(f"Data successfully written to {csv_file_path}")


def main() -> None:
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Call ABC model API and handle JSON input/output.")
    parser.add_argument('input_file', help="Path to the JSON input file")
    parser.add_argument('-o', '--output_file', help="Path to save the output JSON", default=None)
    parser.add_argument('-c', '--csv_file', help="Path to save the output CSV", default=None)
    parser.add_argument('-t', '--timeout', type=int, help="Request timeout in seconds", default=10)
    parser.add_argument('--show_headers', action='store_true', help="Show response headers in the output")
    parser.add_argument('--url', help="API URL", default='https://fastabc-57h9n.ondigitalocean.app/abc')
    parser.add_argument('--output_csv', action='store_true', help="Output results as CSV")
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
        response_data = response.json()
        pretty = json.dumps(response_data, indent=2)

        if args.output_file:
            save_output(args.output_file, pretty)
        else:
            print(pretty)

        # Output CSV if requested
        if args.output_csv and args.csv_file:
            with open(args.output_file if args.output_file else 'response.json', 'w') as json_file:
                json_file.write(pretty)
            output_json_to_csv(args.output_file if args.output_file else 'response.json', args.csv_file)

    else:
        logging.error(f'Response error: {response.status_code}')
        logging.error(response.text)


if __name__ == '__main__':
    main()
