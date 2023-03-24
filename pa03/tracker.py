# offers the user the following options and makes calls to the Transaction class to update the database.

from transaction import Transaction

menu_options = '''Please select the number corresponding the command:
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date (MM-DD-YYYY)
8. summarize transactions by month (MM)
9. summarize transactions by year (YYYY)
10. summarize transactions by category
11. print this menu
'''

def process_choice(choice):

    if choice=='0': #quit
        return
    elif choice=='1': #show categories
        ctgries = transaction.select_all() #will be changed to transaction.select_all()
        print("Categories:")
        for category in ctgries:
            print(f"- {category}")
    elif choice=='2': #add category
        name = input("name of category: ")
        desc = input("category description: ")
        ctgry = {'name':name, 'desc':desc}
        transaction.add(ctgry) #will be changed to transaction.add()
    elif choice=='3': #modiify category
        print("Modify Category:")
        id = int(input("id: "))
        name = input("new name of category: ")
        desc = input("new category description: ")
        ctgry = {'name':name, 'desc':desc}
        transaction.update(id,ctgry)


    elif choice=='7':
        date=input("Enter the date (MM-DD-YYYY):")
        summary = transaction.summarize_transactions_by_date(date) #Calls the summarize_transaction_by_date method from Transaction class 
        print(f"Transactions on {date}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '8':
        month = input("Enter the month (YYYY-MM): ")
        summary = transaction.summarize_transactions_by_month(month) #Calls the summarize_transaction_by_month
        print(f"Transactions in {month}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '9':
        year = input("Enter the year (YYYY): ")
        summary = transaction.summarize_transactions_by_year(year) #Calls the summarize_transaction_by_year
        print(f"Transactions in {year}:")
        for category, amount in summary.items():
            print(f"- {category}: {amount}")
    elif choice == '10':
        category = input("Enter the category: ")
        summary = transaction.summarize_transactions_by_category(category)
        print(f"Transactions in '{category}':")
        for date, amount in summary.items():
            print(f"- {date}: {amount}")
    elif choice=='11':
        print(menu_options)

    else:
        print("Invalid choice, try again")
        toplevel()

    choice = input("> ")
    return(choice)



def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu_options)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('THE END')




    


#add to transaction, delete later
def select_all(self):
    con= sqlite3.connect(self.dbfile)
    cur = con.cursor()
    cur.execute("SELECT rowid,* from categories")
    tuples = cur.fetchall()
    con.commit()
    con.close()
    return to_cat_dict_list(tuples)


        