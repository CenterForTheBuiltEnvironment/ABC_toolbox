import json
import jsonschema2md

parser = jsonschema2md.Parser(
    examples_as_yaml=False,
    show_examples="all",
)
file_path = "C:\\Users\\monyo\\PycharmProjects\\ABC_JSON_schema\\json schema\\abc-schema-V1.json"

with open(file_path, "r") as json_file:
    md_lines = parser.parse_schema(json.load(json_file))
print(''.join(md_lines))
