# json_examples/json_basic.py
import sys
import json

data = {
    'big_number': 2 ** 3141,
    'max_float': sys.float_info.max,
    'a_list': [2, 3, 5, 7],
}

json_data = json.dumps(data)
print(json_data)
data_out = json.loads(json_data)
print(data_out)
assert data == data_out  # json and back, data matches