###financetracker103
##Description:

##Running pytest: 
 pytest test_transaction.py
================================================= test session starts =================================================
platform win32 -- Python 3.8.5, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\Users\yalda\desktop\financetracker103\pa03
collected 8 items

test_transaction.py ........                                                                                     [100%]

================================================== 8 passed in 0.28s ==================================================

 pytest test_category.py
================================================= test session starts =================================================
platform win32 -- Python 3.8.5, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\Users\yalda\desktop\financetracker103\pa03
collected 4 items

test_category.py ....                                                                                            [100%]

================================================== 4 passed in 0.76s ==================================================
PS C:\Users\yalda\desktop\financetracker103\pa03>


Pylint tests:

category: 10/10
test_category: 8.33/10
test_transaction: 8.5/10 - Only problem was something to do with db_file, but could not change it without tests failing
tracker: 8.67/10
transaction.py: 9.56/10
