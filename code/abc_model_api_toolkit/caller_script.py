from abc_model_api_client import call_abc_model_api
from data_processor import output_json_to_csv

def main(
        input_json_file,
        output_json_file,
        output_csv_file,
        api_url='https://fastabc-57h9n.ondigitalocean.app/abc'
):
    call_abc_model_api(input_json_file, output_json_file, api_url)
    output_json_to_csv(output_json_file, output_csv_file)

if __name__ == '__main__':
    main(
    input_json_file = r'C:\Users\monyo\PycharmProjects\ABC_JSON_schema\test\abc_function_test_ramp.json',
    output_json_file = r'C:\Users\monyo\PycharmProjects\ABC_JSON_schema\test\abc_function_test_ramp_output.json',
    output_csv_file = r'C:\Users\monyo\PycharmProjects\ABC_JSON_schema\test\abc_function_test_ramp_output.csv',
)