from pymongo import MongoClient
import datetime as dt
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create a database
db = client['hackathon']

# Create a collection
transactions_collection = db['transactions']

# CRUD operations for transactions

def create_transaction(transaction_data):
    try:
        result = transactions_collection.insert_one(transaction_data)
        return result.inserted_id
    except Exception as e:
        print(f"Error creating transaction: {e}")
        return None

def read_transaction(transaction_id):
    try:
        transaction = transactions_collection.find_one({"_id": transaction_id})
        return transaction
    except Exception as e:
        print(f"Error reading transaction: {e}")
        return None

def update_transaction(transaction_id, updated_data):
    try:
        result = transactions_collection.update_one({"_id": transaction_id}, {"$set": updated_data})
        return result.modified_count
    except Exception as e:
        print(f"Error updating transaction: {e}")
        return 0

def delete_transaction(transaction_id):
    try:
        result = transactions_collection.delete_one({"_id": transaction_id})
        return result.deleted_count
    except Exception as e:
        print(f"Error deleting transaction: {e}")
        return 0
    
#get transactions by user id
def get_transactions_by_user_id(user_id):
    try:
        transactions = transactions_collection.find({'user_id': user_id})
        return transactions
    except Exception as e:
        print(f"Error getting transactions by user id: {e}")
        return None
    
    
def get_transactions_analytics_by_year(year):
    try:
        #fetch transactions done in the given year, start date = 1st jan and end date = 31st dec
        transactions = transactions.find({'date': {'$gte': f'{year}-01-01', '$lt': f'{year+1}-01-01'}}) 
    except Exception as e:
        print(f"Error getting transactions by year: {e}")
        return None  
    return

def get_yearly_wise_summary(user_id):
    try:
        #fetch transactions done in the given year, start date = 1st jan and end date = 31st dec
        all_transactions = transactions_collection.find({'user_id': user_id})
        summary = {}
        for transaction in all_transactions:
            year = dt.datetime.strptime(transaction['time'], '%d-%m-%Y').year
            if year not in summary:
                summary[year] = 0
            summary[year] += transaction['amount']
    except Exception as e:
        print(f"Error getting yearly wise summary: {e}")
        return None
    return summary