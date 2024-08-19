# json_schema
This folder contains a Python script that converts JSON schema files into Markdown format. 
The generated Markdown files are used for the input and output sections in the official documentation.

## How to Use
To update the official documentation based on changes to the JSON schema files, follow these steps:

1. **Edit the JSON Schema Files**: Make the necessary updates to the JSON schema files (`abc_input_schema_v1.json` and/or `abc_output_schema_v1.json`). Change the file name (for example `abc_input_schema_v2.json`) and move to the old file to `old` directory.

2. **Run the Script**:
   - Ensure you have Python installed, along with the required dependencies.
   - Execute `main.py`:
     ```bash
     python main.py
     ```
   - This will convert the updated JSON schema files into Markdown files (`abc_input_schema_v1.markdown` and `abc_output_schema_v1.markdown`), which can be directly used in the official documentation.

## Requirements

- Python 3
- `jsonschema2md` package

Install the required package using pip:

```bash
pip install jsonschema2md
```