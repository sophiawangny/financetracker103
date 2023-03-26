
"""transaction.py is a Object Relational Mapping to the transactions table
    This app will store the data in a SQLite database ~/trans.db
"""
import sqlite3

def to_dict(trans):
    #areen
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('transaction='+str(trans))
    result = {'itemid':trans[0], 'amount':trans[1],
    'category':trans[2], 'date':trans[3], 'description':trans[4]}
    return result


def transaction_list(transaction_tuples):
    #Yalda
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_dict(transaction) for transaction in transaction_tuples]

class Transaction:
    ''' Transaction represents a table of transaction'''
    def __init__(self):
        self.database = sqlite3.connect('trans.db')
        self.run_query('''CREATE TABLE IF NOT EXISTS transaction
                          (itemid real, amount real, category text, date text, description text)''')

    def add_transaction(self, itemid, amount, category, date, description):
        #areen
        ''' add a transaction to the transactions table.'''
        self.run_query('''
            INSERT INTO transaction 
            (itemid, amount, category, date, description) 
            VALUES (?, ?, ?, ?, ?)
        ''', (itemid, amount, category, date, description))

    def delete_transaction(self, itemid):
        #areen
        ''' delete a transaction with a specified item id'''
        self.run_query('''DELETE FROM transaction WHERE itemid = ?''', (itemid,))

    def get_transactions(self):
        #Yalda
        '''returns a list of transactions'''
        cursor = self.database.cursor()
        cursor.execute('''SELECT * FROM transaction''')
        transactions = cursor.fetchall()
        return [to_dict(t) for t in transactions]

    def get_transactions_by_date(self, date):
        #areen
        '''returns a list of transactions by date'''
        query = '''SELECT * FROM transaction WHERE date = ?'''
        return self.database.execute(query, (date,)).fetchall()

    def get_transactions_by_category(self, category):
        #areen
        '''returns a list of transactions by category'''
        return self.database.execute('''
            SELECT * 
            FROM transaction 
            WHERE category = ?
            ''', (category,)).fetchall()


    def select_all(self):
        #Yalda
        ''' return all of the transactions as a list of dicts.'''
        cursor = self.database.cursor()
        cursor.execute('''SELECT name FROM categories''')
        return cursor.fetchall()

    def add_category(self, category):
        #Yalda
        ''' add a category to the table.'''
        cursor = self.database.cursor()
        query = '''INSERT INTO categories(name, description) VALUES(?, ?)'''
        values = (category['name'], category['desc'])
        cursor.execute(query, values)
        self.database.commit()

    def update_category(self, id_num, category):
        #Yalda
        '''modify a category in the table.'''
        cursor = self.database.cursor()
        query = '''UPDATE categories SET name = ?, description = ? WHERE id_num = ?'''
        values = (category['name'], category['desc'], id_num)
        cursor.execute(query, values)
        self.database.commit()

    def run_query(self, query, params=None):
        '''execute a SQL query on the database'''
        if params is None:
            params = []
        cursor = self.database.cursor()
        cursor.execute(query, params)
        self.database.commit()
        return cursor.fetchall()



if __name__ == "__main__":
    transaction=Transaction()
