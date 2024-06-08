from flask import Blueprint, jsonify,request
from models.transactions import get_yearly_wise_summary
analytics =  Blueprint('analytics', __name__,url_prefix='/v1')


#endpoint to get transaction data of user by time period
@analytics.route('/analytics/<user_id>', methods=['GET'])
def get_transactions_analytics(user_id):
    
    summary = get_yearly_wise_summary(user_id)
    
    return jsonify(summary), 200