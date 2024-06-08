from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create a database
db = client['hackathon']

# Create a collection
users_collection = db['users']


def create_user(user):
    try:
        users_collection.insert_one(user)
        return True
    except Exception as e:
        print(e)
        return False
    

# Get all users
def get_all_users():
    try:
        return users_collection.find()
    except Exception as e:
        print(e)
        return False
    

# Get a user by id
def get_user_by_id(user_id):
    return users_collection.find_one({'id': user_id})

# Update a user
def update_user(user_id, new_values):
    update_query = {'id': user_id}
    users_collection.update_one(update_query, new_values)

# Delete a user
def delete_user(user_id):
    delete_query = {'id': user_id}
    users_collection.delete_one(delete_query)
    read_user = users_collection.find_one({'id': 1})
    print(read_user)

