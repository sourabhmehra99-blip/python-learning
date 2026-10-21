# dictionary
# person_dict = {
#     "name":"Sourabh Mehra",
#     "class":"B.Tech CSE Branch",
#     "skill":["python","C++","github","git"]
# }

# JSON: A string form a dictionary

# person_json = "{'name':'Sourabh Mehra','class':'B.tech CSE Branch','skill':['python','C++','github','git']}"

# Changing Dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.

import json as jo
# python dictionary

person_dict = {
    "name":"Sourabh Mehra",
    "class":"B.Tech CSE Branch",
    "skill":["python","C++","github","git"]
}

# let's convert it to  json
person_josn = jo.dumps(person_dict,indent =4)
print(type(person_josn))
print(person_josn)

# output --

# <class 'str'>
# {
#     "name": "Sourabh Mehra",
#     "class": "B.Tech CSE Branch",
#     "skill": [
#         "python",
#         "C++",
#         "github",
#         "git"
#     ]
# }