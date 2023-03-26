'''The Transaction class for handling SQL commands'''
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
                          (itemid real, amount real, category text, 
                          date text, description text)''',())

    def add_transaction(self, itemid, amount, category, date, description):
        #Areen
        ''' add a transaction to the transactions table.'''
        self.runQuery('''
            INSERT INTO transactions (itemid, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (itemid, amount, category, date, description))

    def delete_transaction(self, itemid):
        #Areen
        ''' delete a transaction with a specified item id'''
        self.runQuery('DELETE FROM transactions WHERE itemid = ?', (itemid,))

    def get_transactions(self):
        #Yalda
        '''returns a list of transactions'''
        return self.runQuery('''SELECT * FROM transactions''', ()).fetchall()
   

    def get_transactions_by_date(self, date):
        #Areen
        '''returns a list of transactions by date'''
        query = '''SELECT * FROM transactions WHERE date = ?'''
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

    def to_month(self, date):
        '''converts string to a date and gets the month'''
        #Omar
        format = '%Y-%m-%d'  # The format, can be changed depending on what is used
        datetimestr = datetime.datetime.strptime(date, format)
        return datetimestr.month

    def to_year(self, date):
        '''converts string to a date and gets the year'''
        #Omar
        format = '%Y-%m-%d' # The format, can be changed depending on what is used
        datetimestr = datetime.datetime.strptime(date, format)
        return datetimestr.year


    def select_all(self):
        #Yalda
        ''' return all of the transactions as a list of dicts.'''
        conn = sqlite3.connect("transactions.db")
        c = conn.cursor()
        c.execute("SELECT DISTINCT category FROM transactions")
        categories = [category[0] for category in c.fetchall()]
        conn.close()
        return categories

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
        con= sqlite3.connect('transactions.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()

        return [to_dict(t) for t in tuples]
        # return True

if __name__ == "__main__":
    transactions=Transaction()
