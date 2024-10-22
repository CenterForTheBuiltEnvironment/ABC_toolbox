# ABC model toolbox
Useful toolbox for the Advanced Berkeley Comfort (ABC) model.
Please see the README file in each folder for instructions on how to use each toolkit.

## Toolbox
The current toolbox includes the following tool and documentation:
 - `abc_model_api_toolkit`: Python package for handling ABC model API.
 - `abc_model_excel_toolkit`: Python package for connecting ABC model to Microsoft Excel.
 - `abc_model_json_schema_toolkit`: JSON schema for ABC model's input and output files.
 - `abc_model_logo`: For image files for ABC's logo
 - `abc_model_official_documentation`: Official documentation for ABC model. Synced with Gitbook.


## How to install

Follow these steps to set up the virtual environment and install the necessary packages for this project.

### 1. Clone the Repository
Clone this repository to your local machine (you can set up this using you IDE as well):
```bash
git clone https://github.com/CenterForTheBuiltEnvironment/ABC_toolbox.git
```

### 2. Make sure the Project Directory
Please make sure the project directory. If you are not be there, move into the cloned repository directory:
```bash
cd ABC_toolbox
```
###  3. Create a Virtual Environment
Create a Python virtual environment:
```bash
python -m venv env
```

###  4. Activate the Virtual Environment
Activate the virtual environment.

For Mac/Linux:
```bash
source env/bin/activate
```

For Windows:
```bash
env\Scripts\activate
```

###  5. Install the Required Packages
While inside the virtual environment, install the necessary packages using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Contact
If you find any errors on this toolbox, please post the issue [here](https://github.com/CenterForTheBuiltEnvironment/ABC_toolbox/issues).
Or, email to the project's administrators: Charlie Huizenga (huizenga@berkeley.edu) and Akihisa Nomoto (monyo323232@gmail.com)

## License
The all tools in this toolbox are under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).