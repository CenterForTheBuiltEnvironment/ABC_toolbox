import requests
import json
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_json_file(file_path: str) -> str:
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Error: File not found - {file_path}")
        raise
    except IOError as e:
        logging.error(f"Error: Unable to read file {file_path} - {e}")
        raise


def post_json_data(
    url: str, data: str, headers: dict, timeout: int
) -> requests.Response:
    try:
        return requests.post(url, data=data, headers=headers, timeout=timeout)
    except requests.exceptions.Timeout:
        logging.error(f"Error: The request timed out after {timeout} seconds.")
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")
        raise


def save_output(file_path: str, data: str) -> None:
    try:
        with open(file_path, "w") as file:
            file.write(data)
        logging.info(f"Output has been saved to {file_path}")
    except IOError as e:
        logging.error(f"Error: Unable to write to file {file_path} - {e}")
        raise


def call_abc_model_api(input_file: str, output_file: str, url: str, timeout: int = 10):
    input_text = read_json_file(input_file)
    headers = {"Content-Type": "application/json"}
    response = post_json_data(url, input_text, headers, timeout)
    if response.status_code == 200:
        save_output(output_file, response.text)
    else:
        logging.error(f"Response error: {response.status_code}")
        logging.error(response.text)
        response.raise_for_status()
