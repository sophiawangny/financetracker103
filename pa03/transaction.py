class Transaction:
    def __init__(self, filename):
        self.cnct = sqlite3.connect(filename)