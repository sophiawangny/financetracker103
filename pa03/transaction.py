def toDict(t):
    #areen
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('t='+str(t))
    transaction = {'itemid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction:
    def __init__(self, filename):
        self.cnct = sqlite3.connect(filename)

    #suggester __init__(self, filename) fro lecture 19 like the professor asked in mastery
    #def __init__(self):
    #   self.runQuery('''CREATE TABLE IF NOT EXISTS transaction
    #               (amount text, category text, date text, description text)''',())
    #amount might be int
    #    return self.runQuery("UPDATE transaction SET completed=1 WHERE rowid=(?)",(rowid,))
    #should we set the date of transaction to Datetime.now()
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        #areen
        con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]