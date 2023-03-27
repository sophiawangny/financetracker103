'''
test_transactions runs unit and integration tests on the transactions module
'''
import pytest
import os
from datetime import datetime
from transaction import Transaction

@pytest.fixture
def db_file():
	#Sophia
    db_file = 'test_transactions.db'
    yield db_file
    os.remove(db_file)


def test_init(db_file):
    transaction = Transaction(db_file)
    assert os.path.exists(db_file)


def test_select_all(db_file):
	#Sophia
    transaction = Transaction(db_file)
    assert len(transaction.select_all()) == 0

    itemid = transaction.add_transaction(1, 100, 'food', '2022-03-25', 'groceries')
    assert len(transaction.select_all()) == 1
    assert transaction.select_all()[0]['itemid'] == itemid
    assert transaction.select_all()[0]['amount'] == 100
    assert transaction.select_all()[0]['category'] == 'food'
    assert transaction.select_all()[0]['date'] == '2022-03-25'
    assert transaction.select_all()[0]['description'] == 'groceries'

def test_add_transaction(db_file):
	#Yalda
    transaction = Transaction(db_file)
    itemid = transaction.add_transaction(1, 100, 'food', '2022-03-25', 'groceries')
    assert itemid == 1

def test_delete_transaction(db_file):
	#Yalda
    transaction = Transaction(db_file)
    itemid = transaction.add_transaction(1, 100, 'food', '2022-03-25', 'groceries')
    assert len(transaction.select_all()) == 1

    transaction.delete_transaction(itemid)
    assert len(transaction.select_all()) == 0

def test_get_transactions_by_date(db_file):
	#Yalda
    transaction = Transaction(db_file)
    transaction.add_transaction(1, 100, 'food', '2022-03-25', 'groceries')
    transaction.add_transaction(2, 200, 'entertainment', '2022-03-26', 'movie')
    transaction.add_transaction(3, 50, 'food', '2022-03-27', 'restaurant')

    assert len(transaction.get_transactions_by_date('2022-03')) == 3
    assert len(transaction.get_transactions_by_date('2022-04')) == 0
    assert len(transaction.get_transactions_by_date('2022-03-25')) == 1

def test_get_transactions_by_category(db_file):
	#Omar
    transaction = Transaction(db_file)
    transaction.add_transaction(1, 100, 'food', '2022-03-25', 'groceries')
    transaction.add_transaction(2, 200, 'entertainment', '2022-03-26', 'movie')
    transaction.add_transaction(3, 50, 'food', '2022-03-27', 'restaurant')

    result = transaction.get_transactions_by_category()
    assert result['food'] == 150
    assert result['entertainment'] == 200

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

 




