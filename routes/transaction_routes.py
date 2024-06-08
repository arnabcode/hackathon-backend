from flask import Blueprint, jsonify,request
import time
import datetime as dt
from models.transactions import create_transaction ,get_transactions_by_user_id

transactions =  Blueprint('transactions', __name__,url_prefix='/v1')
transaction = {
    'id': 1,
    'amount': 1000,
    'time': '2021-09-01 12:00:00',
    'category': 'Food',
    'merchant': 'McDonalds',
    'user_id': 1
}

def generate_id():
    return int(time.time() * 1000)

@transactions.route('/transaction', methods=['POST'])
def create_new_transaction():
    data = request.get_json()
    transaction_id = generate_id()
    transaction = {
        'id': transaction_id,
        'amount': data['amount'],
        'time': data['time'],
        'category': data['category'],
        'merchant': data['merchant'],
        'user_id': data['user_id']
    }
    create_transaction(transaction)
    return jsonify({'message': 'Transaction created successfully', 'transaction': transaction}), 201

# @transactions.route('/transactions', methods=['GET'])
# def get_transactions():
#     all_transactions = get_all_transactions()
#     return jsonify({'transactions': all_transactions}), 200

# @transactions.route('/transactions/<transaction_id>', methods=['GET'])
# def get_transaction(transaction_id):
#     transaction = get_transaction_by_id(transaction_id)
#     if transaction:
#         return jsonify({'transaction': transaction}), 200
#     else:
#         return jsonify({'message': 'Transaction not found'}), 404


#get transactions by user id
@transactions.route('/transactions/user/<user_id>', methods=['GET'])
def get_transactions_by_user(user_id):
    transactions = get_transactions_by_user_id(user_id)
    return jsonify({'transactions': transactions}), 200
    
    


@transactions.route('/read-csv', methods=['GET'])
def read_csv():
    import pandas as pd
    data = pd.read_csv('MOCK_DATA.csv')
    transactions = []
    for index, row in data.iterrows():
       
        transaction = {
            'id': generate_id(),
            'amount': row['amount'],
            #remove AM/PM from time
            
            'time': dt.datetime.strptime(f"{row['date']} {row['time']}", '%m-%d-%Y %I:%M %p').strftime('%m-%d-%Y %H:%M'),
            
            'category': row['category'],
            'merchant': row['merchant'],
            'user_id': row['user_id']
        }
        transactions.append(transaction)
    return jsonify({'transactions': transactions[:5]}), 200

@transactions.route('/read-csv-add', methods=['GET'])
def read_csv_add():
    import pandas as pd
    data = pd.read_csv('MOCK_DATA.csv')
    
    for index, row in data.iterrows():
        time = row['time'].split(' ')[0]
        transaction = {
            'id': generate_id(),
            'amount': row['amount'],
            'time':  dt.datetime.strptime(f"{row['date']} {row['time']}", '%m-%d-%Y').strftime('%m-%d-%Y'),
            
            'category': row['category'],
            'merchant': row['merchant_name'],
            'user_id': row['user_id']
        }
        
        create_transaction(transaction)
    return jsonify({'message': 'Transactions added successfully'}), 200




