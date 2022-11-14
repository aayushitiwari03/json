import json
py={"Name ":"Abhishek","Designation ":"CEO of navgurukul","Gender ":"male","Age ":"29"}
f=open("Text.json","w")
json.dump(py,f)


