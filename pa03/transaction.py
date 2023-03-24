import sqlite3
import os

def toDict(t):
    #areen
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('t='+str(t))
    transaction = {'itemid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction:
    ##def __init__(self, filename):
    #    self.cnct = sqlite3.connect(filename)

    #suggested __init__(self, filename) fro lecture 19 like the professor asked in mastery
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS trans
                   (amount text, category text, date text, description text)''',())
        
    #amount might be int
        #return self.runQuery("UPDATE transaction SET completed=1 WHERE rowid=(?)",(rowid,))
    #should we set the date of transaction to Datetime.now()

    
    #def add(self,item):
    #    #areen
    #    ''' create a transaction item and add it to the transaction table '''
    #    return self.runQuery("INSERT INTO transaction VALUES(?,?,?)",(item['amount'],description['desc'],item['date']))

    #def delete(self,rowid):
    #    #areen
    #    ''' delete a transaction item '''
    #    return self.runQuery("DELETE FROM transaction WHERE itemid=(?)",(itemid,))
    

    def add_transaction(self, itemid, amount, category, date, description):
        #areen
        self.runQuery('''
            INSERT INTO transaction (itemid, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (itemid, amount, category, date, description))

    def delete_transaction(self, transaction_id):
        #areen
        self.runQuery('DELETE FROM transaction WHERE itemid = ?', (itemid,))

    def get_transactions_by_date(self, date):
        return self.run_query('SELECT * FROM transactions WHERE date = ?', (date,))
    
    def get_transactions_by_category(self, category):
        return self.run_query('SELECT * FROM transactions WHERE category = ?', (category,))

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
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        #areen
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
