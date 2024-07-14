"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
from datastructures import FamilyMember
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

member_one = FamilyMember("John", "33 years old", [7,13,22])
member_two = FamilyMember("Jane", "35 years old", [10,14,3])
member_three = FamilyMember("Jimmy", "5 years old", [1])


jackson_family.add_member(member_one)
jackson_family.add_member(member_two)
jackson_family.add_member(member_three)

# for member in jackson_family._members:
#     print(f"{member.id}: {member.first_name} / {jackson_family.last_name} / {member.age} / {member.lucky_numbers}")
        

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    if not members:
        return "wrong info", 400
    
    response_body = {
        "family": jackson_family.last_name,
        "members": members
    }

    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_user_by_id(id):
    member = jackson_family.get_member(id)
    if not member:
        return "wrong info", 400
    
    response_body = {
        "family": jackson_family.last_name,
        "member" : member
    }

    return jsonify(response_body), 200

@app.route('/add_member', methods=['POST'])
def add_user():
    data = request.get_json()
    first_name = data.get("first_name")
    age = data.get("age")
    lucky_numbers = data.get("lucky_numbers")
    new_member = FamilyMember(first_name,age,lucky_numbers)
    jackson_family.add_member(new_member)
    
    if not first_name or not age or not lucky_numbers:
        return "wrong info", 400

    return jsonify(new_member.to_dict()), 200

@app.route('/delete_member/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    deleted_member = jackson_family.delete_member(id)
    if not deleted_member:
        return "wrong info", 400

    return jsonify(deleted_member.to_dict()), 200
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 30000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
