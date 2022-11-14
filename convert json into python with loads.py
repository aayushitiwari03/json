
# import json

# a='{"lalalala": 3}'
# print(type(a))
# mystring = json.loads(a)
# print(type(mystring))

import json

dict1 ='{"emp1": {"name": "Lisa","designation": "programmer","age": "34","salary": "54000"},"emp2": {"name": "Elis","designation": "Trainee","age": "24","salary": "40000"}}'
print(type(dict1))
python=json.loads(dict1)
print(type(python))