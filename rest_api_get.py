# 1. import the pieces we need
from flask import Flask,request, jsonify

# 2. create the app
app = Flask(__name__)

# 3. some sample data to return (a Python list)
students=[

    {"Id":2,"Name": "Nawal","Roll":5},
    {"Id":1,"Name": "Adiba","Roll":10},
    {"Id":3,"Name": "Hridi","Roll":3},
    {"Id":4,"Name": "Mabs","Roll":2},
    {"Id":5,"Name": "Momo","Roll":7},
    {"Id":6,"Name": "Barisha","Roll":12}
]
@app.route('/')
def home():
    return "Hello! Welcome to my API!! Write /student to get data"
@app.route('/student',methods=['GET'])
def get():
   return jsonify(students)
# 4. route: when someone visits /items with GET, run the function below
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
   for student in students:
    if student["Id"]==student_id:
     return jsonify(student)
    return jsonify({"Error!": "No student found"})
@app.route('/add_std',methods=['POST'])
def add_student():
   data = request.get_json()
   students.append(data)
   return jsonify(data),201

# 5. start the server when we run this file directly
if __name__ == '__main__':
    app.run(debug=True)
