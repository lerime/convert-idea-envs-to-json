import json
import xmltodict
import pprint
import sys

def parse_envs(data: dict):
    resp = {}
    for item in data['env']:
        resp[item['@name']] = item['@value']
    return resp

def write_to_json_file(data, filename):
    json_object = json.dumps(data, indent=4)
    
    with open(filename, "w") as outfile:
        outfile.write(json_object)

output_filename = "sample.json"

if len(sys.argv) == 1 :
    pprint.pp("Please specify a filename")
    sys.exit(0)
elif len(sys.argv) > 2:
    output_filename = sys.argv[2]

file_name = sys.argv[1]

with open(file_name, 'r', encoding='utf-8') as file:
	my_xml = file.read()

my_dict = xmltodict.parse(my_xml)

pprint.pprint(my_dict, indent=2)

print(20 * "*")

env_data = parse_envs(my_dict['component']['configuration']['envs'])
pprint.pprint(env_data)

write_to_json_file(env_data, output_filename)
