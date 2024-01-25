import json

student_info = {
    "name": "kabila",
    "age": 21,
    "phoneno": "8144883952",
    "cgpa": 8.19
}
# Convert to JSON
json_obj = json.dumps(student_info)
print(json_obj)

l=open("sample.json","w")
l.write(json_obj)
print(l)
