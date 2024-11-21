# ABC model Excel toolkit

## Overview
This toolkit has Python code to convert Excel input to JSON input and code to run ABC model in Excel format.

 - - `__init__.py`: Initialization file.
 - `abc_example.xlsm`: The Excel workbook has been developed to use the Advanced Berkeley Comfort (ABC) model within Excel. By entering measured values such as air temperature, relative humidity, and radiant temperature into the model, you can evaluate the thermal comfort of the environment.
 - `abc_excel_to_json.py`: Python code to convert Excel input to JSON input
 - `main.py`: Main code. When you click on "Simulate" bottom in the Excel file, this code will run.