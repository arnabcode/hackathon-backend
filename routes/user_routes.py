from flask import Blueprint, jsonify,request
import time
from models.users import create_user, get_all_users, get_user_by_id, update_user, delete_user


user =  Blueprint('user', __name__,url_prefix='/v1')
#funtion to generate timestamp based unique id of user

def generate_id():
    return int(time.time() * 1000)


@user.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    print(data)
    #prepare user data
    
    user = {
        
        'name': data['name'],
        'email': data['email'],
        'age': data['age'],
        'gender': data['gender'],
        
        
    }
    
    result =  create_user(user)
    
    if result:
        return jsonify({'message': 'User added successfully'}), 200
    else:
        return jsonify({'message': 'Failed to add user'}), 500
     
     
     
#add multiple users 
@user.route('/users/multiple', methods=['POST'])
def add_multiple_users():
    data = request.get_json()
    for user in data['users']:
        user_data = {
            'name': user['name'],
            'email': user['email'],
            'age': user['age'],
            'gender' : user['gender'],
        }
        create_user(user_data)
    return jsonify({'message': 'Users added successfully'}), 200


#get all users
@user.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    users_list = []
    for user in users:
        temp_user = {}
        temp_user['_id'] = str(user['_id'])
        temp_user['name'] = user['name']
        temp_user['email'] = user['email']
        temp_user['age'] = user['age']
        temp_user['gender'] = user['gender']
        users_list.append(temp_user)
    return jsonify({'users': users_list}), 200