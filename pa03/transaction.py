def toDict(t):
    ''' t is a tuple ('item id','amount','category','date','description')'''
    print('t='+str(t))
    transaction = {'itemid':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction:
    def __init__(self, filename):
        self.cnct = sqlite3.connect(filename)
