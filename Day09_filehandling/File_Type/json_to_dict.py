# hanging JSON to Dictionary
# To change a JSON to a dictionary, first we import the json module and
#  then we use loads method.

import json as jo
# JSON
person_json = '''{
    "name": "Sourabh",
    "country": "India",
    "city": "indore",
    "skills": ["C++", "C", "Python"]
}'''

# change JSON to dictionary we use loads key word

person_dict = jo.loads(person_json)
print(type(person_dict))
print(person_dict)
print(person_dict['name'])

# Output
# <class 'dict'>
# {'name': 'Sourabh', 'country': 'India', 'city': 'indore', 'skills': ['C++', 'C', 'Python']}
# Sourabh