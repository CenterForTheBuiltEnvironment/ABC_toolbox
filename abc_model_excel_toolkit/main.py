import os
import pandas as pd
import xlwings as xw

# Add the parent directory to sys.path to ensure correct imports
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Importing from abc_model_api_toolkit
from abc_model_api_toolkit.api_client import call_abc_model_api
from abc_model_api_toolkit.data_processor import output_json_to_csv

# Importing from abc_model_excel_toolkit
from abc_model_excel_toolkit.abc_excel_to_json import EXCELtoJSONConverter


wb = xw.books.active
ws = wb.sheets["Results"]

# Get the full path of the active Excel workbook
excel_file_path = wb.fullname

# Get the file name without extension
file_name = os.path.splitext(os.path.basename(excel_file_path))[0]


def run_abc(
    input_json_file,
    output_json_file,
    output_csv_file,
    api_url="https://fastabc-57h9n.ondigitalocean.app/abc",
):
    call_abc_model_api(input_json_file, output_json_file, api_url)
    output_json_to_csv(output_json_file, output_csv_file)


def import_csv_to_excel(csv_file_path):

    # Clear the Results sheet
    ws.clear_contents()

    # Load CSV data into the Results sheet
    df = pd.read_csv(csv_file_path)

    # Write the CSV data to Excel, including column headers
    ws.range("A1").value = [df.columns.tolist()]  # Write column headers
    ws.range("A2").value = df.values.tolist()  # Write data

    print(f"CSV data imported to Results sheet.")


if __name__ == "__main__":
    # Paths for input/output files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print("current dir:", current_dir)

    # Create a tmp directory for storing files
    temp_dir = os.path.join(current_dir, "tmp")

    input_json_file = os.path.join(temp_dir, f"input_{file_name}.json")
    output_json_file = os.path.join(temp_dir, f"output_result_{file_name}.json")
    output_csv_file = os.path.join(temp_dir, f"output_result_{file_name}.csv")

    # Step 1: Convert Excel to JSON
    converter = EXCELtoJSONConverter(excel_file_path)
    converter.to_json(input_json_file)

    # Step 2: Call API and get CSV
    run_abc(input_json_file, output_json_file, output_csv_file)

    # Step 3: Import CSV to Excel Results sheet
    import_csv_to_excel(output_csv_file)

    print("All processes completed successfully.")
