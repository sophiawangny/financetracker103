import sqlite3
import os
import datetime

def to_dict(trans):
    #Areen
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
    #Areen
    ''' Transaction represents a table of transaction'''
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                          (itemid real, amount real, category text, date text, description text)''',())
    

    def add_transaction(self, itemid, amount, category, date, description):
        #Areen
        ''' add a transaction to the transactions table.'''
        self.runQuery('''
            INSERT INTO transaction (itemid, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (itemid, amount, category, date, description))

    def delete_transaction(self, transaction_id):
        #Areen
        ''' delete a transaction with a specified item id'''
        self.runQuery('DELETE FROM transaction WHERE itemid = ?', (itemid,))

    def get_transactions(self):
        #Yalda
        '''returns a list of transactions'''
        temp = self.runQuery('''SELECT * FROM transaction''')
        transactions = temp.fetchall()
        return [to_dict(t) for t in transactions]

    def get_transactions_by_date(self, date):
        #Areen
        '''returns a list of transactions by date'''
        query = '''SELECT * FROM transaction WHERE date = ?'''
        return self.runQuery(query, (date,)).fetchall()
    
    def get_transactions_by_category(self, category):
        #Areen
        '''returns a list of transactions by category'''
        return self.runQuery('SELECT * FROM transactions WHERE category = ?', (category,))
    
    def get_transactions_by_month(self, month):
        #Omar
        '''returns a dictionary of transactions by category for the given month'''
        return self.runQuery('SELECT * FROM transactions WHERE to_month(date) = ?', (month,))
    
    def get_transactions_by_year(self, year):
        #Omar
        '''returns a dictionary of transactions by category for the given year'''
        return self.runQuery('SELECT * FROM transactions WHERE to_year(date) = ?', (year,))

    def to_month(date):
        #Omar
        format = '%Y-%m-%d'  # The format, can be changed depending on what is used
        datetimestr = datetime.datetime.strptime(date, format)
        return datetimestr.month
    
    def to_year(date):
        #Omar
        format = '%Y-%m-%d' # The format, can be changed depending on what is used
        datetimestr = datetime.datetime.strptime(date, format)
        return datetimestr.year
    '''
    def modify_transaction(self, itemif, amount=None, category=None, date=None, description=None):
        #areen
        update_query = 'UPDATE transaction SET '
        update_args = []
        if amount is not None:
            update_query += 'amount = ?, '
            update_args.append(amount)
        if category is not None:
            update_query += 'category = ?, '
            update_args.append(category)
        if date is not None:
            update_query += 'date = ?, '
            update_args.append(date)
        if description is not None:
            update_query += 'description = ?, '
            update_args.append(description)
        update_query = update_query.rstrip(', ')
        update_query += ' WHERE itemid = ?'
        update_args.append(itemid)
        self.runQuery(update_query, tuple(update_args))
    '''

    def select_all(self):
        #Yalda
        ''' return all of the transactions as a list of dicts.'''
        cursor = self.runQuery('''SELECT name FROM categories''')
        return cursor.fetchall()

    def add_category(self, category):
        #Yalda
        ''' add a category to the table.'''
        query = '''INSERT INTO categories(name, description) VALUES(?, ?)'''
        values = (category['name'], category['description'])
        cursor = self.runQuery(query, values)
        return

    def modify_category(self, id_num, category):
        #Yalda
        '''modify a category in the table.'''
        query = '''UPDATE categories SET name = ?, description = ? WHERE id_num = ?'''
        values = (category['name'], category['description'], id_num)
        cursor= self.runQuery(query, values)
        return
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        #Areen
        con= sqlite3.connect('trans.db')
        
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        
        return [toDict(t) for t in tuples]
        # return True

if __name__ == "__main__": 
    transaction=Transaction()
