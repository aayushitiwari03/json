a={"simi":2,"riti":4}
import json
with open("file.json","w") as b:
    a=json.dump(a,b,indent=7)