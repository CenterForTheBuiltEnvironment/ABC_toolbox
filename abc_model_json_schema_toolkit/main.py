import os
import json
import jsonschema2md
from datetime import datetime

# Constants for file paths
CURRENT_DIRECTORY = os.getcwd()
INPUT_SCHEMA_FILE_NAME = "abc_input_schema_v1"
OUTPUT_SCHEMA_FILE_NAME = "abc_output_schema_v1"

INPUT_JSON_SCHEMA_FILE_PATH = (
    f"{os.path.join(CURRENT_DIRECTORY, INPUT_SCHEMA_FILE_NAME)}.json"
)
OUTPUT_JSON_SCHEMA_FILE_PATH = (
    f"{os.path.join(CURRENT_DIRECTORY, OUTPUT_SCHEMA_FILE_NAME)}.json"
)

INPUT_MARKDOWN_FILE_PATH = (
    f"{os.path.join(CURRENT_DIRECTORY, INPUT_SCHEMA_FILE_NAME)}.markdown"
)
OUTPUT_MARKDOWN_FILE_PATH = (
    f"{os.path.join(CURRENT_DIRECTORY, OUTPUT_SCHEMA_FILE_NAME)}.markdown"
)


def save_schema_as_markdown(json_file_path, markdown_file_path):
    """
    Converts a JSON schema to a Markdown file and appends the current time to the description.

    :param json_file_path: Path to the JSON schema file.
    :param markdown_file_path: Path to save the Markdown formatted schema.
    :return: None
    """
    parser = jsonschema2md.Parser(examples_as_yaml=False, show_examples="all")

    with open(json_file_path, "r") as json_file:
        schema = json.load(json_file)

    # Add current datetime to the schema description
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "description" in schema:
        schema["description"] += f" (Generated on {current_time})"
    else:
        schema["description"] = f"Generated on {current_time}"

    with open(markdown_file_path, "w") as md_file:
        markdown_content = parser.parse_schema(schema)
        md_file.write("".join(markdown_content))
        print(f"Markdown content successfully written to {markdown_file_path}")


if __name__ == "__main__":
    save_schema_as_markdown(
        json_file_path=INPUT_JSON_SCHEMA_FILE_PATH,
        markdown_file_path=INPUT_MARKDOWN_FILE_PATH,
    )
    save_schema_as_markdown(
        json_file_path=OUTPUT_JSON_SCHEMA_FILE_PATH,
        markdown_file_path=OUTPUT_MARKDOWN_FILE_PATH,
    )
