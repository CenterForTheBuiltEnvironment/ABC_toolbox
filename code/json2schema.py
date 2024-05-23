import json
import genson


def generate_json_schema_from_data(data: Any) -> Dict:
    builder = genson.SchemaBuilder()
    builder.add_object(data)
    schema = builder.to_schema()
    return schema


input_path = "C:\\Users\\monyo\\PycharmProjects\\ABC_JSON_schema\\json schema\\abc-schema-V1.json"
schema = generate_json_schema_from_data(data=input_path)
print(json.dumps(schema, indent=2))
