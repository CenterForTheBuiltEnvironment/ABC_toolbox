from flask import Flask, request, jsonify
import os
from data_processor import process_json  # Import your processor

app = Flask(__name__)


@app.route("/convert-file", methods=["POST"])
def convert_file():
    json_file_path = request.json.get(
        "json_file_path"
    )  # Pass the JSON file path as an argument in the request body
    csv_output_path = "output.csv"

    # Call the process_json function and convert the file
    process_json(
        output_json_file_path=json_file_path,
        csv_output=True,
        csv_file_path=csv_output_path,
    )

    return jsonify({"message": "CSV conversion completed", "csv_file": csv_output_path})


if __name__ == "__main__":
    app.run(debug=True)
