from flask import request, jsonify

def greet_func(username):
    return f'Hello, {username}!' , 200

def farewell_func(username):
    return f'GoodBye {username}!' , 200

def read_func():
    return 'Reading Data Sunccessfully' , 200

def create_func():
    data = request.get_json()
    return jsonify({
        "message":"POST method working fine",
        "data":data
    }),201

def update_func(id):
    data = request.get_json()
    return jsonify({
        "Message":"PATCH method working fine",
        "data":data,
        "id":f"This is your params {id}"
    }),200

def delete_func(id):
    return jsonify({
            "Message":"DELETE method working fine",
            "id":f"This is your params {id}"
        }),200