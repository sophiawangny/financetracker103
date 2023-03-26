'''
test_transactions runs unit and integration tests on the transactions module
'''

import pytest
from transaction import Transaction
transaction = Transaction()

@pytest.fixture
def transaction():
    return Transaction()

def test_add_transaction(transaction):
	#Yalda
    transaction.add_transaction(1, 10, 'Clothing', '2022-03-25', 'Bought a white t-shirt in the mall')
    transactions = transaction.get_transactions()
    assert len(transactions) == 1
    assert transactions[0]['itemid'] == 1
    assert transactions[0]['amount'] == 10
    assert transactions[0]['category'] == 'Clothing'
    assert transactions[0]['date'] == '2022-03-25'
    assert transactions[0]['description'] == 'Bought a white t-shirt in the mall'

def test_delete_transaction(transaction):
	#Yalda
    transaction.add_transaction(1, 10, 'food', '2022-03-25', 'Bought pizza')
    transaction.delete_transaction(1)
    transactions = transaction.get_transactions()
    assert len(transactions) == 0


def test_get_transactions_by_date(transaction):
	#Yalda
    transaction.add_transaction(1, 10, 'food', '2022-03-25', 'Bought pizza')
    transaction.add_transaction(2, 20, 'clothing', '2022-03-26', 'Bought a shirt')
    transaction.add_transaction(2, 4, 'Drinks', '2022-03-26', 'Bought a coffee')

    transactions = transaction.get_transactions_by_date('2022-03-26')
    assert len(transactions) == 2

def test_get_transactions_by_year(transaction):
    #areen
    transaction.add_transaction(1, 10, 'food', '2022-03-25', 'Bought pizza')
    transaction.add_transaction(2, 20, 'clothing', '2022-03-26', 'Bought a shirt')
    transaction.add_transaction(2, 4, 'Drinks', '2022-03-26', 'Bought a coffee')

    transactions = transaction.get_transactions_by_year('2022')
    assert len(transactions) == 3

def test_get_transactions_by_month(transaction):
    #areen
    transaction.add_transaction(1, 10, 'food', '2022-03-25', 'Bought pizza')
    transaction.add_transaction(2, 20, 'clothing', '2022-03-26', 'Bought a shirt')
    transaction.add_transaction(2, 4, 'Drinks', '2022-03-26', 'Bought a coffee')

    transactions = transaction.get_transactions_by_year('03')
    assert len(transactions) == 3

def test_add_category(transaction):
    transaction.add_category({'name': 'food', 'description': 'Groceries'})
    categories = transaction.select_all()
    assert len(categories) == 1
    assert categories[0][0] == 'food'
    
def test_modify_category(transaction):
    transaction.add_category({'name': 'food', 'desc': 'Groceries and eating out'})
    transaction.modify_category(1, {'name': 'drinks', 'desc': 'Beverages'})
    categories = transaction.select_all()
    assert len(categories) == 1
    assert categories[0][0] == 'drinks'


def test_to_month(transaction): #sophia
    transaction.to_month('2001-02-04')
    assert '2'

def test_to_year(transaction): #sophia
    transaction.to_year('2001-02-04')
    assert '2001'



def test_modify_category(self, transaction):#sophia

    # define the test category
    category = {'name': 'School', 'desc': 'category for my school supplies'}

    # add the test category to the database
    cat_id = transaction.add_category(category)

    # modify the category
    new_category = {'name': 'School supplies', 'desc': 'all my school supplies'}
    transaction.modify_category(cat_id, new_category)

    # retrieve the modified category from the database
    result = transaction.get_category_by_id(cat_id)

    # assert that the modified category has the correct values
    self.assertEqual(result['name'], 'School supplies')
    self.assertEqual(result['desc'], 'all my school supplies')


