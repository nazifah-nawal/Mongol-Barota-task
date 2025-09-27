import requests

url = "http://127.0.0.1:5000/add_std"

# The new student data we want to add
new_student = {
    "Id": 7,
    "Name": "Charlie",
    "Roll": 103
}

# Send POST request
response = requests.post(url, json=new_student)

# Print response from server
print(response.status_code)  # Should print 201
print(response.json())       # Should print the student we added


