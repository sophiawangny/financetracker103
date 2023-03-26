import sqlite3
import os

def toDict(t):
    #areen
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('t='+str(t))
    transaction = {'itemid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction


###Yalda 
def transaction_list(transaction_tuples):
    return [toDict(transaction) for transaction in transaction_tuples]

class Transaction:

   def __init__(self):
        self.db = sqlite3.connect('trans.db')
        self.runQuery('''CREATE TABLE IF NOT EXISTS transaction
                          (itemid real, amount real, category text, date text, description text)''')


    

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
        self.runQuery('''INSERT INTO transaction (itemid, amount, category, date, description)
                         VALUES (?, ?, ?, ?, ?)''', (itemid, amount, category, date, description))


    def delete_transaction(self, itemid):
        #areen
        self.runQuery('''DELETE FROM transaction WHERE itemid = ?''', (itemid,))


    ###Yalda
    def get_transactions(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT * FROM transaction''')
        transactions = cursor.fetchall()
        return [toDict(t) for t in transactions]


    def get_transactions_by_date(self, date):
        #areen
        return self.db.execute('''SELECT * FROM transaction WHERE date = ?''', (date,)).fetchall()
    

    def get_transactions_by_category(self, category):
        #areen
        return self.db.execute('''SELECT * FROM transaction WHERE category = ?''', (category,)).fetchall()


    ######we dont need this method?
    # def modify_transaction(self, itemif, amount=None, category=None, date=None, description=None):
    #     #areen
    #     update_query = 'UPDATE transaction SET '
    #     update_args = []
    #     if amount is not None:
    #         update_query += 'amount = ?, '
    #         update_args.append(amount)
    #     if category is not None:
    #         update_query += 'category = ?, '
    #         update_args.append(category)
    #     if date is not None:
    #         update_query += 'date = ?, '
    #         update_args.append(date)
    #     if description is not None:
    #         update_query += 'description = ?, '
    #         update_args.append(description)
    #     update_query = update_query.rstrip(', ')
    #     update_query += ' WHERE itemid = ?'
    #     update_args.append(itemid)
    #     self.runQuery(update_query, tuple(update_args))



     ###Yalda 
    def select_all(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT name FROM categories''')
        return cursor.fetchall()


    ###Yalda
	def add_category(self, category):
    	cursor = self.db.cursor()
    	cursor.execute('''INSERT INTO categories(name, description) VALUES(?, ?)''', (category['name'], category['desc']))
    	self.db.commit()

 

    ###Yalda
 	def update_category(self, id, category):
    	cursor = self.db.cursor()
    	cursor.execute('''UPDATE categories SET name = ?, description = ? WHERE id = ?''', (category['name'], category['desc'], id))
    	self.db.commit()


    
    def runQuery(self, query, params=None):
        # execute a SQL query on the database
        if params is None:
            params = []
        cursor = self.db.cursor()
        cursor.execute(query, params)
        self.db.commit()
        return cursor.fetchall()


if __name__ == "__main__": 
    transaction=Transaction()
