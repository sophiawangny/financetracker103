'''The Transaction class for handling SQL commands'''
import sqlite3
import os
import datetime

def to_dict(trans):
    #Areen
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('transaction='+str(trans))
    transaction = {'itemid':trans[0], 'amount':trans[1],
    'category':trans[2], 'date':trans[3], 'description':trans[4], 'category': trans[5]}
    return transaction

def transaction_list(transaction_tuples):
    #Yalda
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_dict(transaction) for transaction in transaction_tuples]

class Transaction:
    #Areen
    ''' Transaction represents a table of transaction'''
    def __init__(self, dbfile):
        #Sophia
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (itemid real, amount real, date text, description text, category text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile


    def select_all(self):
        #Sophia
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT itemid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return transaction_list(tuples)


    def add_transaction(self, itemid, amount, category, date, description):
        #Areen
        ''' add a transaction to the transactions table.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",
                    (transaction['itemid'], transaction['amount'],
                        transaction['date'], transaction['description'],  transaction['category']))
        con.commit()
        cur.execute('SELECT last_insert_rowid()')
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete_transaction(self, itemid):
        #Areen
        ''' delete a transaction with a specified item id'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("DELETE FROM transactions WHERE itemid=(?)", (itemid,))
        con.commit()
        con.close()
   

    def get_transactions_by_date(self, date):
        #Areen
        '''returns a list of transactions by date'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #date format is MM-DD-YYYY
        cur.execute("SELECT date FROM transactions WHERE date LIKE ?", ('%'+date+'%',))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return transaction_list(tuples)

    def get_transactions_by_category(self, category):
        #Yalda
        '''returns a list of transactions by category'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT category, sum(amount) FROM transactions GROUP BY category")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict(tuples)

    def get_transactions_by_month(self, month):
        #Omar
        '''returns a dictionary of transactions by category for the given month'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT date FROM transactions WHERE date LIKE ?", (month+'-%',))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_trans_dict_list(tuples)

    def get_transactions_by_year(self, year):
        #Omar
        '''returns a dictionary of transactions by category for the given year'''
        return self.runQuery('SELECT * FROM transactions WHERE to_year(date) = ?', (year,))

if __name__ == "__main__":
    transactions=Transaction()
