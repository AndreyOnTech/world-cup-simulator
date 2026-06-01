import json

with open("grupos_copa.json", "r", encoding="utf-8") as file:
    groups = json.load(file)

print(groups)